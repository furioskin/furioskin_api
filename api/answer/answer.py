from typing import List

from fastapi import APIRouter, Depends, Query

from app.answer.schemas import CreateAnswerResponseSchema, CreateAnswerRequestSchema
from app.answer.services import AnswerService
from app.question.models import Question
from app.question.schemas import GetQuestionListResponseSchema, CreateQuestionRequestSchema, \
    CreateQuestionResponseSchema, GetQuestionResponseSchema
from app.question.services import QuestionService

answer_router = APIRouter()


@answer_router.post(
    "",
    response_model=CreateAnswerResponseSchema,
)
async def create_answer(request: CreateAnswerRequestSchema):
    await AnswerService().create_answer(**request.dict())
    return {"content": request.content, "userId": request.userId, "questionId": request.questionId}

