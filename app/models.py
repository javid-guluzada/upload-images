from sqlalchemy import Column, Integer, String, LargeBinary
from .database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    data = Column(LargeBinary)
    mime_type = Column(String)
