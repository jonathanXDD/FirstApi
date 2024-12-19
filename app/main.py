from fastapi import FastAPI
from app.database import Base,engine
from app.routers import router
#initialize 

app = FastAPI()

#initialze Database`s table
Base.metadata.create_all(bind=engine)

#register Router
app.include_router(router=router,prefix="/api",tags=["todos"])

