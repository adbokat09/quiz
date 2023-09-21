class AnswerOption:
    def __init__(self, text: str, is_correct: bool, score: int = 0):
        self.text = text
        self.is_correct = is_correct
        self.score = score

    @classmethod
    def create_from_dict(cls, data: dict) -> 'AnswerOption':
        return cls(
            text=data['text'],
            is_correct=data['is_correct'],
            score=data['score']
        )

