from pydantic import BaseModel
from datetime import datetime

class LoginResponse(BaseModel):
  access_token: str
