from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import database, engine, metadata
from routers import IncludeRoutes

@asynccontextmanager
async def lifespan(app: FastAPI):  
  await database.connect()
  metadata.create_all(engine)
  yield
  await database.disconnect()

app = FastAPI(lifespan=lifespan)
IncludeRoutes(app)
