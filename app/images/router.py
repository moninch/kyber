import shutil

from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import JSONResponse

from app.users.dependencies import get_current_user

from app.users.models import Users


router = APIRouter(prefix="/images", tags=["Loading images"])


@router.post("/posts")
async def add_image_to_post(
    image_name: str,
    image_file: UploadFile,
    current_admin_user: Users = Depends(get_current_user),
):
    image_path = f"app/static/images/{image_name}.webp"

    with open(image_path, "wb+") as file_object:
        shutil.copyfileobj(image_file.file, file_object)

    # await process_pic.delay(image_path)

    return JSONResponse(
        status_code=201, content={"detail": "Image uploaded successfully"}
    )
