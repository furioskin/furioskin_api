from sqlalchemy import Column, Unicode, BigInteger, Boolean

from core.db import Base
from core.db.mixins import TimestampMixin


class Board(Base, TimestampMixin):
    __tablename__ = "boards"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    userId = Column(BigInteger, nullable=False)
    categoryId = Column(BigInteger, nullable=False)
    categoryName = Column(Unicode(10000))
    content = Column(Unicode(10000))
