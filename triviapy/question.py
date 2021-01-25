class Question(object):
    def __init__(self, question, answer, answers, category, difficulty):
        self.question = question
        self.answer = answer
        self.answers = answers
        self.category = category
        self.difficulty = difficulty
