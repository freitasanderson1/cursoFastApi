from auth.serializers import LoginRequest, LoginResponse
from fastapi import HTTPException, status


class UserServices:
  async def login(self, data: LoginRequest) -> LoginResponse:
    user = await self.__get_user(data.email)
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado!")
    if not self.__verify_password(data.password, user["password"]):
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Senha incorreta!")
    return {"token": self.__generate_token(user["id"])}  