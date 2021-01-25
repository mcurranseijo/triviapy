class TokenError(ValueError):
    def __init__(self):
        self.strerror = "TokenError"
        self.args = {"A token could not be generated."}


class QuestionError(ValueError):
    def __init__(self):
        self.strerror = "QuestionError"
        self.args = {"Not enough questions avaliable."}


class InvalidTokenError(ValueError):
    def __init__(self):
        self.strerror = "InvalidToken"
        self.args = {"Token is invalid or has expired."}


class CategoryError(ValueError):
    def __init__(self):
        self.strerror = "CategoryError"
        self.args = {"Category given is invalid"}
