from typing import Optional, List

from sqlalchemy import or_, select, and_

from app.doctor.models import Doctor
from app.user.models import User
from app.user.schemas.user import LoginResponseSchema
from core.db import Transactional, session
from core.number import get_random_int


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
            raise 1/0

        doctor = Doctor(id=get_random_int(), userId=user_id, hospital=hospital)
        session.add(doctor)

