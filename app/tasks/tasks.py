import smtplib
from pathlib import Path
from PIL import Image
from pydantic import EmailStr
from app.config import settings
from app.tasks.celery import celery

  
  

@celery.task

def process_pic(
    path: str,
):
    im_path = Path(path) # конвертируем обычную строку в Path
    im = Image.open(im_path) # Получаем изображение по этому пути
    im_resized_1000_500 = im.resize((1000,500))
    im_resized_200_100 = im.resize((200,100))
    im_resized_1000_500.save(f"app/static/images/resized1000_500_{im_path.name}")
    im_resized_200_100.save(f"app/static/images/resized1200_100_{im_path.name}")