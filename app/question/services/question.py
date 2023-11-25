from typing import Optional, List

from sqlalchemy import or_, select, and_

from app.question.models import Question
from app.user.schemas.user import LoginResponseSchema
from core.db import Transactional, session


class QuestionService:
    def __init__(self):
        ...

    async def get_question_list(
        self,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[Question]:

        query = select(Question)

        if prev:
            query = query.where(Question.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()


    async def get_question(
        self,
        question_id: int
    ) -> List[Question]:

        query = select(Question).where(Question.id == question_id)
        result = await session.execute(query)
        return result.scalars().all()

    @Transactional()
    async def create_question(
        self, content: str, userId: int
    ) -> None:

        question = Question(content=content, userId=userId)
        session.add(question)

