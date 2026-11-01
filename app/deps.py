import os
import secrets
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

load_dotenv()
API_KEY = os.environ["API_KEY"]

apikey_scheme = APIKeyHeader(name="X-API-Key")

def verify_api_key(key: str = Depends(apikey_scheme)):
    credentials_error = HTTPException(status_code=401, detail="Could not validate credentials")
    if not secrets.compare_digest(API_KEY, key):
        raise credentials_error