from typing import Optional, List

from sqlalchemy import or_, select, and_

from app.doctor.models import Doctor
from app.user.models import User
from app.user.schemas.user import LoginResponseSchema
from core.db import Transactional, session
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailOrNicknameException,
    UserNotFoundException,
)
from core.exceptions.user import UserAlreadyDoctorException
from core.utils.token_helper import TokenHelper


class DoctorService:
    def __init__(self):
        ...

    @Transactional()
    async def create_doctor(
        self, user_id: int, hospital: str
    ) -> None:

        query = select(Doctor).where(Doctor.userId == user_id)
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise UserAlreadyDoctorException

        doctor = Doctor(userId=user_id, hospital=hospital)
        session.add(doctor)

