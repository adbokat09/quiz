from typing import List

from quiz.question import Question


class Quiz:
    def __init__(self, topic: str, questions: List[Question]):
        self.topic = topic
        self.questions: List[Question] = questions
        self._current_question_index: int = 0

    def __repr__(self):
        return f'Quiz {self.topic}'

    @classmethod
    def create_from_dict(cls, data: dict) -> "Quiz":
        return cls(
            topic=data['topic'],
            questions=[Question.create_from_dict(q) for q in data['questions']]
        )

    @property
    def current_question(self):
        return self.questions[self._current_question_index]

    def show_question(self):
        print(f'Питання №{self._current_question_index + 1}:')
        self.current_question.display()

    def has_next_question(self) -> bool:
        return self._current_question_index < len(self.questions) - 1

    def next_question(self):
        self._current_question_index += 1

    def wait_user_answer(self):
        answer = input('Ваша відповідь:')
        self.current_question.evaluate_answer(answer)

    def show_result(self):
        total_score = 0
        for question in self.questions:
            print(question)
            question.show_user_answer()
            total_score += question.user_score

        print(f'Ваша загальна кількість балів: {total_score}')


