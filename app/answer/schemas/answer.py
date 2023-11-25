from pydantic import BaseModel, Field


class GetAnswerListResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")
    questionId: int = Field(..., description="questionId")

    class Config:
        orm_mode = True


class CreateAnswerRequestSchema(BaseModel):
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")
    # questionId: int = Field(..., description="questionId")


class CreateAnswerResponseSchema(BaseModel):
    content: str = Field(..., description="content")
    userId: int = Field(..., description="userId")
    questionId: int = Field(..., description="questionId")

    class Config:
        orm_mode = True

