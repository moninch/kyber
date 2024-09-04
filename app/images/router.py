import shutil

from fastapi import APIRouter, Depends, UploadFile

from app.tasks.tasks import process_pic
from app.users.dependencies import get_current_admin_user
from app.users.models import Users

router = APIRouter(
    prefix='/images',
    tags=["Загрузка картинок"]
)

@router.post("/posts")
async def add_posts_image(name: str, file: UploadFile, current_user : Users = Depends(get_current_admin_user)):
    im_path = f'app/static/images/{name}.webp'
    with open(f"{im_path}", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(im_path)


