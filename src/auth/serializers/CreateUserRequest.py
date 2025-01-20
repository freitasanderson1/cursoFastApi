from pydantic import BaseModel

class CreateUserRequest(BaseModel):
  username: str
  password: str
  is_admin: bool = False
  is_superuser: bool = False
  active: bool = True