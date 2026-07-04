import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET = os.getenv("AWS_S3_BUCKET")

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB_NAME")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME")

QUEUE_URL = os.getenv("SQS_QUEUE_URL")

BASE_S3_PREFIX = os.getenv("BASE_S3_PREFIX")

print("AWS_ACCESS_KEY_ID :", AWS_ACCESS_KEY_ID)
print("AWS_SECRET_ACCESS_KEY :", AWS_SECRET_ACCESS_KEY)
print("AWS_REGION :", AWS_REGION)
print("BUCKET :", BUCKET)

print()

print("MONGO_URI :", MONGO_URI)
print("DB_NAME :", DB_NAME)
print("COLLECTION_NAME :", COLLECTION_NAME)

print()

print("QUEUE_URL :", QUEUE_URL)
print("BASE_S3_PREFIX :", BASE_S3_PREFIX)