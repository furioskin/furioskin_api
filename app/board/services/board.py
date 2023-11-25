from app.board.models import Board
from core.db import Transactional, session
from typing import Optional, List
from sqlalchemy import or_, select, and_


class BoardService:
    def __init__(self):
        ...

    @Transactional()
    async def create_board(
        self, user_id: int, category_id: int, content: str
    ) -> None:

        board = Board(userId=user_id, categoryId=category_id, content=content)
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