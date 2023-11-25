from pydantic import BaseModel, Field


class GetBoardListResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    userId: int = Field(..., description="userId")
    categoryId: int = Field(..., description="categoryId")
    categoryName: str = Field(..., description="categoryName")
    content: str = Field(..., description="content")

    class Config:
        orm_mode = True


class CreateBoardRequestSchema(BaseModel):
    userId: int = Field(..., description="userId")
    categoryId: int = Field(..., description="categoryId")
    categoryName: str = Field(..., description="categoryName")
    content: str = Field(..., description="content")


class CreateBoardResponseSchema(BaseModel):
    userId: int = Field(..., description="userId")
    categoryId: int = Field(..., description="categoryId")
    categoryName: str = Field(..., description="categoryName")
    # content: str = Field(..., description="content")

    class Config:
        orm_mode = True