from make_question_interface.IMakeQuestion import IMakeQuestion
from make_question_interface.Results import Results

class MakeQuestionStorage(IMakeQuestion):
    def __init__(self, make_question: IMakeQuestion):
        self._make_question = make_question

    def make_question(self, question: str):
        self._make_question.make_question(question)

    def get_answer_text_raw(self) -> str:
        return self._make_question.get_answer_text_raw()

    def get_results(self) -> Results:
        return self._make_question.get_results()

    def get_implementation_alias(self) -> str:
        return self._make_question.get_implementation_alias()
