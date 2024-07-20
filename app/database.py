import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS =os.getenv("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS,tlsAllowInvalidCertificates=True)
database = client.my_database
images_collection = database.get_collection("images")
