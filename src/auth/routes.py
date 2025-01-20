from fastapi import APIRouter, status

from auth.serializers import LoginRequest, LoginResponse, CreateUserRequest
from auth.services import UserServices

service = UserServices()

router = APIRouter(prefix='/auth', tags=["auth"])

@router.get("/check/{username}", status_code=status.HTTP_200_OK)
async def get_user(username: str):
  user = await service.get_user(username)
  avaliable = False if user else True  
  return {"avaliable": avaliable}

@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(data: LoginRequest):
  return await service.login(data)

@router.post("/register", response_model=LoginResponse, status_code=status.HTTP_201_CREATED)
async def register(data: CreateUserRequest):
  return await service.create_user(data)
