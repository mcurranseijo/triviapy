from random import shuffle
from html import unescape

from .utils import request_json
from .errors import TokenError, QuestionError, InvalidTokenError, CategoryError
from .question import Question
from .urls import TOKEN_URL, RESET_URL, CATEGORY_URL, QUESTION_BASIC, QUESTION_TOKEN


class Game(object):
    def __init__(self):
        self.token = ""

    async def catetgories(self):
        """
        Returns an array of tuples with the category and their id's used to request them.
        """
        data = await request_json(CATEGORY_URL)
        categories = []

        for category in data["trivia_categories"]:
            categories.append((category["name"], category["id"]))
        return categories

    async def gen_token(self):
        """
        Use this to generate a token, this is an optional step but will keep questions from repeating.
        """
        data = await request_json(TOKEN_URL)

        if data["response_code"] == 0:
            self.token = data["token"]
        else:
            raise TokenError

    async def round(self, qty=1, category=0):
        """
        Use this to get questions, takes in a catgegory
        """
        if self.token and category:
            url = QUESTION_TOKEN.format(qty, self.token, category)
        elif not self.token and category:
            url = QUESTION_BASIC.format(qty, category)
        data = await request_json(url)

        if data["response_code"] == 1:
            raise QuestionError
        elif data["response_code"] == 2:
            raise CategoryError
        elif data["response_code"] == 3:
            raise InvalidTokenError
        elif data["response_code"] == 4:
            raise QuestionError

        questions = []
        for question in data["results"]:
            answers = question["incorrect_answers"]
            answers.append(question["correct_answer"])
            shuffle(answers)
            questions.append(
                Question(
                    question=unescape(question["question"]),
                    answer=unescape(question["correct_answer"]),
                    answers=unescape(answers),
                    category=unescape(question["category"]),
                    difficulty=unescape(question["difficulty"]),
                )
            )

        if len(questions) > 1:
            return questions
        else:
            return questions[0]

    async def reset(self):
        """
        Use this to reset a token and allow old questions to be seen again.
        """
        if not self.token:
            return

        url = RESET_URL.format(self.token)
        print(url)
        data = await request_json(RESET_URL.format(self.token))

        if data["response_code"] == 0:
            self.token = data["token"]
        else:
            raise TokenError
