from pydantic import BaseModel, Field


class QuestionResponse(BaseModel):
    id: int = Field(..., description="Id")
    content: str = Field(..., description="Content")
    userId: int = Field(..., description="userId")