from fastapi import APIRouter
from starlette.staticfiles import StaticFiles

from api.answer.answer import answer_router
from api.file.file import file_router
from api.questions.question import question_router
from api.user.v1.user import user_router as user_v1_router
from api.auth.auth import auth_router

router = APIRouter()
router.include_router(user_v1_router, prefix="/users", tags=["User"])
# router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(question_router, prefix="/questions", tags=["Question"])
router.include_router(answer_router, prefix="/answers", tags=["Answer"])
router.include_router(file_router, prefix="/file", tags=["File"])

router.mount("/static", StaticFiles(directory="static"), name="static")

__all__ = ["router"]
