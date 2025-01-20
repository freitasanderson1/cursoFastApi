from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from database import database, engine, metadata
from routers import IncludeRoutes
from auth.security import Auth

@asynccontextmanager
async def lifespan(app: FastAPI):  
  await database.connect()
  metadata.create_all(engine)
  yield
  await database.disconnect()

auth = Auth()
app = FastAPI(lifespan=lifespan)
IncludeRoutes(app)

@app.middleware("http")
async def check_authentication(request: Request, call_next):
  token = request.headers.get("Authorization")
  if not await auth.check_permissions(request.method, request.url.path, token):
    return JSONResponse(status_code=403, content={"message": "You are not authorized to access this resource"})
  return await call_next(request)