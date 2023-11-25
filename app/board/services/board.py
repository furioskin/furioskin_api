from app.board.models import Board
from core.db import Transactional, session
from typing import Optional, List
from sqlalchemy import or_, select, and_

from core.number import get_random_int


class BoardService:
    def __init__(self):
        ...

    @Transactional()
    async def create_board(
        self, userId: int, categoryId: int, content: str, categoryName: str
    ) -> None:

        board = Board(id=get_random_int(),userId=userId, categoryId=categoryId, content=content, categoryName=categoryName)
        session.add(board)


    async def get_board_list(
        self,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[Board]:

        query = select(Board)

        if prev:
            query = query.where(Board.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()