from sqlalchemy import Column, Unicode, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class Answer(Base, TimestampMixin):
    __tablename__ = "answers"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    content = Column(Unicode(1000))
    questionId = Column(BigInteger)
    userId = Column(BigInteger)
