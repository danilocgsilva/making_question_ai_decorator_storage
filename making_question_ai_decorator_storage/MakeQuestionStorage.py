from make_question_interface.IMakeQuestion import IMakeQuestion
from make_question_interface.Results import Results

# SQLAlchemy imports for storage
from .db import get_db
from .models import QuestionRecord

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

    def store_question_record(self, *, question: str, serialized_answer: str = None,
                             result_answer: str = None, timestamp_start: float = None,
                             timestamp_end: float = None, implementation_name: str = None,
                             json_answer: str = None, json_parameters: str = None,
                             json_hardware: str = None):
        """Persist a question record to the database.

        Parameters correspond to columns defined in ``schema.txt`` and the
        ``QuestionRecord`` model. Only ``question`` is required; other fields are
        optional and default to ``None``.
        """
        db_gen = get_db()
        with db_gen as db:
            record = QuestionRecord(
                question=question,
                serialized_answer=serialized_answer,
                result_answer=result_answer,
                timestamp_start=timestamp_start,
                timestamp_end=timestamp_end,
                implementation_name=implementation_name,
                json_answer=json_answer,
                json_parameters=json_parameters,
                json_hardware=json_hardware,
            )
            db.add(record)
            db.commit()
            db.refresh(record)
            return record

