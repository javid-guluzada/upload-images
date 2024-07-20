from pydantic import BaseModel

class ImageMetadata(BaseModel):
    name: str
    mime_type: str
    data: str
