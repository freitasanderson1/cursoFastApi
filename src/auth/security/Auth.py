import jwt
import os
from auth.serializers import LoginRequest

JWT_SECRET = os.getenv('JWT_SECRET')

class Auth:
  def generate_access_token(self, userDict: LoginRequest) -> str:
    return jwt.encode(**dict(userDict), JWT_SECRET, algorithm='HS256')
  
  def decote_access_token(self, token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])