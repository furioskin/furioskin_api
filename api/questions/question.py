from typing import List

from fastapi import APIRouter, Depends, Query

from app.answer.services import AnswerService
from app.question.models import Question
from app.question.schemas import GetQuestionListResponseSchema, CreateQuestionRequestSchema, \
    CreateQuestionResponseSchema, GetQuestionResponseSchema
from app.question.services import QuestionService

question_router = APIRouter()


@question_router.get(
    "",
    response_model=List[GetQuestionListResponseSchema],
)
async def get_question_list(
    limit: int = Query(10, description="Limit"),
    prev: int = Query(None, description="Prev ID"),
):
    return await QuestionService().get_question_list(limit=limit, prev=prev)


@question_router.get(
    "/{question_id}",
    response_model=GetQuestionResponseSchema,
)
async def get_one_question_with_answer(
    question_id: int,
):
    questions = await QuestionService().get_question(question_id)
    if not questions:
        a = 1/0
    question = questions[0]
    answers = await AnswerService().get_answer_list_by_question_id(question_id)
    print(len(answers))
    return {"id": question.id, "content": question.content, "userId": question.userId, "answers": []}
# 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

@question_router.post(
    "",
    response_model=CreateQuestionResponseSchema,
)
async def create_question(request: CreateQuestionRequestSchema):
    await QuestionService().create_question(**request.dict())
    return {"content": request.content, "userId": request.userId}

