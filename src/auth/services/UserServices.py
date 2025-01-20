from auth.serializers import LoginRequest, LoginResponse, CreateUserRequest
from fastapi import HTTPException, status
from databases.interfaces import Record
from database import database
import copy

from auth.model import User
from auth.security import HashPassword, Auth

hash_password = HashPassword()
auth = Auth()

class UserServices:
  async def login(self, data: LoginRequest) -> LoginResponse:
    user = await self.get_user(data.username)
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado!")
    if not hash_password.compair(data.password, user["password"]):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta!")
    return {"access_token": auth.generate_access_token(user)}  
  
  async def get_user(self, username: str) -> Record:
    query = User.select().where(User.c.username == username.lower())
    user = await database.fetch_one(query)
    return user if user else None #HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado!")
  

  async def create_user(self, user: CreateUserRequest) -> Record:
    userExists = await self.get_user(user.username)

    if userExists:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuário já existe!")
    
    user.username = user.username.lower()

    hashed_User = copy.deepcopy(user)
    hashed_User.password = hash_password.hash(user.password)
    hashed_User.is_admin = False
    hashed_User.is_superuser = False
    hashed_User.active = True
    command = User.insert().values(**hashed_User.dict())
    user_id = await database.execute(command)

    return await self.login(LoginRequest(username=user.username, password=user.password))