from sqlalchemy import Column, Integer, Text, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class QuestionRecord(Base):
    __tablename__ = "question_record"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(Text, nullable=False)
    serialized_answer = Column(Text)
    result_answer = Column(Text)
    timestamp_start = Column(Float)
    timestamp_end = Column(Float)
    implementation_name = Column(String(255))
    json_answer = Column(Text)
    json_parameters = Column(Text)
    json_hardware = Column(Text)
    model_name = Column(String(255))
