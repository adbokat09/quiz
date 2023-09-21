from typing import List

from quiz import AnswerOption

class Question:
    def __init__(self, text: str, options: List[AnswerOption]):
        self.text = text
        self.answer_options = options
        self.user_answer = None
        self.user_score = None

    def __repr__(self):
        return f'Question {self.text}'

    @classmethod
    def create_from_dict(cls, data: dict) -> "Question":
        return cls(
            text=data['text'],
            options=[AnswerOption.create_from_dict(o) for o in data['options']],
        )

    def display(self) -> None:
        print(self.text)
        for i, option in enumerate(self.answer_options, 1):
            print(f'{i}) {option.text}')

    def evaluate_answer(self, answer: str) -> float:
        self.user_answer = answer
        answer_option = self.answer_options[int(answer) - 1]
        self.user_score = answer_option.score
        return self.user_score

    def show_user_answer(self):
        if self.user_score > 0:
            print(f'Ваша відповідь {self.user_answer} привильна, ви отримали {self.user_score} балів')
        else:
            print(f'Ви відповіли не правильно ви отримали {self.user_score} балів')


