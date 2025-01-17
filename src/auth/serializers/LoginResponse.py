from pydantic import BaseModel
from datetime import datetime, UTC

class LoginResponse(BaseModel):
  access_token: str
  expires_at: datetime
