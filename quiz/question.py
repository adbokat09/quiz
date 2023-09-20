from typing import List


class Question:
    def __init__(self, text: str, options: List[str], correct_answer: int, score: float = 1):
        self.text = text
        self.answer_options = options
        self.correct_answer = correct_answer
        self.score = score
        self.user_answer = None
        self.user_score = None

    def __repr__(self):
        return f'Question {self.text}. Score {self.score}'

    @classmethod
    def create_from_dict(cls, data: dict) -> "Question":
        return cls(
            text=data['text'],
            options=data['options'],
            correct_answer=data['correct_answer'],
            score=data['score']
        )

    def display(self) -> None:
        print(self.text)
        for i, option in enumerate(self.answer_options, 1):
            print(f'{i}) {option}')

    def evaluate_answer(self, answer: str) -> float:
        self.user_answer = answer
        if int(answer) - 1 == self.correct_answer:
            self.user_score = self.score

        else:
            self.user_score = 0
        return self.user_score

    def show_user_answer(self):
        if self.user_score == self.score:
            print(f'Ваша відповідь {self.user_answer} привильна, ви отримали {self.user_score} балів')
        else:
            print(f'Ви відповіли не правильно ви отримали {self.user_score} балів')


