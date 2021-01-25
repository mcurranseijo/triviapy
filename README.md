# triviapy
triviapy is an async API wrapper for [open trivia database](https://opentdb.com/) this is still a WIP but currently can return questions from specific or all categories and select the number you want to return.


## Setup
1. Make sure you have python installed
2. Download the repository
3. Make sure you have aiohttp installed
4. Place the triviapy folder in your project folder and have fun.


## Quick Start

1. A:First import Game from triviapy and construct a Game object:
```python
from triviapy import Game


game = Game()
```

(optional) Set a game token, this will prevent repeat questions from occuring:
```python
await game.gen_token()
```

2. To see the categories avaliable you can do ``game.categories()``, this returns the below array of category names and ID's,
to use a category supply the number for the category you'd like questions from:
```python
[('General Knowledge', 9), ('Entertainment: Books', 10), ('Entertainment: Film', 11), ('Entertainment: Music', 12), ('Entertainment: Musicals & Theatres', 13), ('Entertainment: Television', 14), ('Entertainment: Video Games', 15), ('Entertainment: Board Games', 16), ('Science & Nature', 17), ('Science: Computers', 18), ('Science: Mathematics', 19), ('Mythology', 20), ('Sports', 21), ('Geography', 22), ('History', 23), ('Politics', 24), ('Art', 25), ('Celebrities', 26), ('Animals', 27), ('Vehicles', 28), ('Entertainment: Comics', 29), ('Science: Gadgets', 30), ('Entertainment: Japanese Anime & Manga', 31), ('Entertainment: Cartoon & Animations', 32)]
```

3. Create a round with question info, you can supply ``qty`` and ``category`` as ints to specify the number of questions and what category you want. It defaults to one question of any category and returns a ``Question`` object if only one if given or an array of them if multiple questions are requested. 
```python
    # This will give 10 questions from the music category.
    round_example = game.round(qty=10, category=12)

    # This will give one question from a random category
    round_2 = game.round()

```

4. Question objects hold all the info needed about a question including: question, category, answers, correct answer, and difficulty:
```python
    question = round_example[0]

    question_str = question.question # Returns the question as a str
    answers = question.answers # Returns a preshuffled array with the 4 multiple choice answer posibilities
    answer = question.answer # Returns the str of the answer, this is included in the answers array as well in the same str format.
    category = question.category # Returns the category of the question as a str
    difficulty = question.difficulty # Returns the question difficulty (Easy, Medium or Hard)

```

5. Error Handling
### Importing errors:
```python
    from triviapy.errors import TokenError, QuestionError, InvalidTokenError, CategoryError
```

### TokenError
This error will occur is ``game.token()`` is unable to set a token, this error may be caused by opentdb outages or other errors.

### QuestionError
This error will occur if the number of questions exceeds that avaliable, when this occurs do ``await game.reset()`` to reuse questions.


### InvalidTokenError
This error is raised due to an invalid or expired token, an api token will expire after 6 hours of no use. Do ``await game.gen_token``` to reset this.

### CategoryError:
This error will occur if an invalid int is defined for a round category. To fix this double check what you are putting in.
