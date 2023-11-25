from typing import List, Optional

from pydantic import BaseModel, Field

from api.answer.response.answer import AnswerResponse


class GetQuestionListResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")

    class Config:
        orm_mode = True


class GetQuestionWithAnswerResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")
    questionId: int = Field(..., description="questionId")

    class Config:
        orm_mode = True

class GetQuestionResponseSchema(BaseModel):
    id: int = Field(..., description="ID")
    content: str = Field(..., description="Content")
    userId: str = Field(..., description="userId")

    class Config:
        orm_mode = True

class CreateQuestionRequestSchema(BaseModel):
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")


class CreateQuestionResponseSchema(BaseModel):
    content: str = Field(..., description="content")
    userId: int = Field(..., description="userId")

    class Config:
        orm_mode = True

