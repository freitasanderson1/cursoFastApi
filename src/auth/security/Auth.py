from auth.serializers import LoginRequest
from dotenv import load_dotenv
from datetime import datetime, timedelta

import jwt
import os

load_dotenv()

JWT_SECRET = os.getenv('JWT_SECRET_TOKEN')

class Auth:
  def generate_access_token(self, userDict: LoginRequest) -> str:
    jwtUserDict = dict(userDict)
    jwtUserDict["expires_at"] = self.expires_at()
    jwtUserDict["signned"] = True

    token = jwt.encode(jwtUserDict, JWT_SECRET, algorithm="HS256")

    return token
  
  async def decode_access_token(self, token: str) -> dict:
    decodeDict = jwt.decode(token, key=JWT_SECRET, algorithms=["HS256"])
    print(f'DecodeDict: {decodeDict}')

    expires_at_obj = datetime.strptime(decodeDict.get("expires_at"), "%Y-%m-%d %H:%M:%S.%f")

    if expires_at_obj <= datetime.now():
      decodeDict.get("signned") == False
      raise jwt.ExpiredSignatureError("Token expired")

    return decodeDict
  
  def expires_at(self):
    return str(datetime.now() + timedelta(days=7))
  
  async def check_permissions(self, method, url, token):

    if method == "GET" and url[1:].split('/')[0] in ['auth','docs']:
      return True
    elif url[1:].split('/')[0] in ['auth','docs']:
      return True
    elif token:
      signned = await self.decode_access_token(token.split(' ')[1])
      return signned.get("signned")
    return False