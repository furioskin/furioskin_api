from sqlalchemy import Column, Unicode, BigInteger, Boolean

from core.db import Base
from core.db.mixins import TimestampMixin


class Doctor(Base, TimestampMixin):
    __tablename__ = "doctors"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    userId = Column(BigInteger, nullable=False)
    hospital = Column(Unicode(255), nullable=False)
