from fastapi import File, UploadFile, APIRouter
from typing import Annotated
from fastapi.responses import FileResponse

file_router = APIRouter()


@file_router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@file_router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@file_router.get("/", response_class=FileResponse)
async def get_file():
    return FileResponse("/Users/dongwon/workspace/fastapi-boilerplate/static/skin.png", media_type="image/png")
