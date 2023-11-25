from fastapi import APIRouter, Depends, Query
from typing import List

from app.board.schemas import GetBoardListResponseSchema, CreateBoardResponseSchema, CreateBoardRequestSchema
from app.board.services import BoardService

board_router = APIRouter()


@board_router.get(
    "",
    response_model=List[GetBoardListResponseSchema]
)
async def get_board_list(
    limit: int = Query(10, description="Limit"),
    prev: int = Query(None, description="Prev ID"),
):
    return await BoardService().get_board_list(limit=limit, prev=prev)

@board_router.post(
    "",
    response_model=CreateBoardResponseSchema
)
async def create_board(request: CreateBoardRequestSchema):
    await BoardService().create_board(**request.dict())
    return {"userId": request.userId, "categoryId": request.categoryId, "categoryName": request.categoryName}
