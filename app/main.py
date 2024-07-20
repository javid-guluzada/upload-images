import base64
import json
import os
from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
import io

from fastapi.staticfiles import StaticFiles

from app.crud import add_image, retrieve_image_by_id, retrieve_images, delete_image
from app.schemas import ImageMetadata

app = FastAPI()
app.mount("/config", StaticFiles(directory="."), name="config")
config_path = os.path.join(os.path.dirname(__file__), '../config.json')

# Load configuration
with open(config_path) as config_file:
    config = json.load(config_file)

ALLOWED_FILE_TYPES = config.get('allowed_file_types', [])

def allowed_file(filename: str) -> bool:
    if not ALLOWED_FILE_TYPES:
        return True  # No restrictions
    return filename.rsplit('.', 1)[-1].lower() in ALLOWED_FILE_TYPES

@app.post("/upload/")
async def upload_image(name: str = Form(...) , file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File type not allowed")

    file_bytes = await file.read()
    image_data = {
        "name": name,
        "mime_type": file.content_type,
        "data": file_bytes
    }

    await add_image(image_data)
    return JSONResponse(content=jsonable_encoder({"message": "Image uploaded successfully"}))

@app.get("/images/")
async def get_images():
    images = await retrieve_images()
    # Encode image data to base64 for easy display in HTML
    for image in images:
        image['data'] = base64.b64encode(image['data']).decode('utf-8')
    return JSONResponse(content=jsonable_encoder(images))

@app.get("/images/{id}")
async def get_image(id: str):
    image = await retrieve_image_by_id(id)  # Implement this function in crud
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    image_data = image['data']
    return StreamingResponse(io.BytesIO(image_data), media_type=image['mime_type'])

@app.delete("/delete/{id}")
async def delete_image_data(id: str):
    deleted = await delete_image(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Image not found")
    return JSONResponse(content={"message": "Image deleted successfully"})

@app.get("/", response_class=HTMLResponse)
async def main():
    with open('app/templates/upload.html', 'r') as file:
        content = file.read()
    return HTMLResponse(content=content)

@app.get("/gallery/", response_class=HTMLResponse)
async def gallery():
    with open('app/templates/gallery.html', 'r') as file:
        content = file.read()
    return HTMLResponse(content=content)
