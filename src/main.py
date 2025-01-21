from contextlib import asynccontextmanager
from fastapi import FastAPI
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