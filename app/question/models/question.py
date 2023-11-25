from sqlalchemy import Column, Unicode, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class Question(Base, TimestampMixin):
    __tablename__ = "questions"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    content = Column(Unicode(1000))
    userId = Column(BigInteger)
