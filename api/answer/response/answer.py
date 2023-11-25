from pydantic import BaseModel, Field


class AnswerResponse(BaseModel):
    id: int = Field(..., description="Id")
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")
    questionId: int = Field(..., description="questionId")