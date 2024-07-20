from motor.motor_asyncio import AsyncIOMotorCollection
from bson import ObjectId
from typing import Dict, List, Optional
from .database import images_collection

# Assuming `images_collection` is defined as an AsyncIOMotorCollection
async def add_image(image_data: Dict) -> str:
    result = await images_collection.insert_one(image_data)
    return  str(result.inserted_id)

async def retrieve_images() -> List[Dict]:
    images_cursor = images_collection.find()
    images = []
    async for image in images_cursor:
        images.append({
            "id": str(image["_id"]),
            "name": image["name"],
            "mime_type": image["mime_type"],
            "data": image["data"]
        })
    return images

async def retrieve_image_by_id(image_id: str) -> Optional[Dict]:
    image = await images_collection.find_one({"_id": ObjectId(image_id)})
    if image:
        return {
            "id": str(image["_id"]),
            "name": image["name"],
            "mime_type": image["mime_type"],
            "data": image["data"]
        }
    return None

async def delete_image(image_id: str) -> bool:
    result = await images_collection.delete_one({"_id": ObjectId(image_id)})
    return result.deleted_count > 0
