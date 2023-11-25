from typing import Optional, List

from sqlalchemy import or_, select, and_

from app.answer.models import Answer
from core.db import Transactional, session
from core.number import get_random_int


class AnswerService:
    def __init__(self):
        ...

    async def get_answer_list(
        self,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[Answer]:

        query = select(Answer)

        if prev:
            query = query.where(Answer.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_answer_list_by_question_id(
        self,
        question_id: int,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[Answer]:

        query = select(Answer).where(Answer.questionId == question_id)

        if prev:
            query = query.where(Answer.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    @Transactional()
    async def create_answer(
        self, content: str, questionId: int, userId: int
    ) -> None:

        answer = Answer(id=get_random_int(), content=content, questionId=questionId, userId=userId)
        session.add(answer)

