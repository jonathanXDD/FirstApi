from fastapi import FastAPI

from .database import Base,engine
from .routers import router
from .auth import router as auth_router

#initialize 

app = FastAPI()

#initialze Database`s table
#Base.metadata.create_all(bind=engine)

#register Router
app.include_router(router=router,prefix="/api",tags=["todos"])
#app.include_router(router=auth_router,prefix="/user",tags=["auth"])
