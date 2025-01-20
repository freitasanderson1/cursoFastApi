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
    token = jwt.encode(jwtUserDict, JWT_SECRET, algorithm="HS256")
    return token
  
  def decode_access_token(self, token: str) -> dict:
    decodeDict = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    parserDatetime = datetime.strftime(decodeDict.get("expires_at"))
    
    print(f'parserDatetime: {parserDatetime}')

    return decodeDict
  
  def expires_at(self):
    return str(datetime.now() + timedelta(days=7))
  
  def check_permissions(self, method, url, token):
    print(f'method: {method} - url {url} - token: {token}')
    return True if method == "GET" and url[1:].split('/')[0] in ['auth','docs'] else False