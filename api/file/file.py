from fastapi import File, UploadFile, APIRouter
from typing import Annotated
from fastapi.responses import FileResponse

file_router = APIRouter()

@file_router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    file_location = f"static/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"filename": file.filename}


@file_router.get("/{file_path}", response_class=FileResponse)
async def get_file(file_path: str):
    file_path = "static/" + file_path
    return FileResponse(file_path, media_type="image/png")

