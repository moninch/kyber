import shutil

from fastapi import APIRouter, UploadFile

from app.tasks.tasks import process_pic

router = APIRouter(
    prefix='/images',
    tags=["Загрузка картинок"]
)

@router.post("/posts")
async def add_posts_image(name: int, file: UploadFile):
    im_path = f'app/static/images/{name}.webp'
    with open(f"{im_path}", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(im_path)


