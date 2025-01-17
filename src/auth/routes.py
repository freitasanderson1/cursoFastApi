from fastapi import APIRouter, status

from auth.serializers import LoginRequest, LoginResponse
from auth.services import UserServices

service = UserServices()

router = APIRouter(prefix='/auth', tags=["auth"])

@router.post("/login", response_model=LoginResponse, status_code=status.HTTP_200_OK)
async def login(data: LoginRequest):
  return await service.login(data)