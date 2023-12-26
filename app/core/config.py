from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "fastapi_chat")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30