from fastapi import File, UploadFile, APIRouter
from typing import Annotated
from fastapi.responses import FileResponse
import httpx
import requests
from requests_toolbelt import MultipartEncoder
from starlette.responses import JSONResponse

file_router = APIRouter()

@file_router.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    file_location = f"static/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    url = "http://14.35.173.13:15834/infer"

    async with httpx.AsyncClient() as client:
        files = {"file": (file.filename, file.file, file.content_type)}
        response = await client.post(url, files=files)
    return response.json()



@file_router.get("/{file_path}", response_class=FileResponse)
async def get_file(file_path: str):
    file_path = "static/" + file_path
    return FileResponse(file_path, media_type="image/png")

