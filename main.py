import uvicorn
from fastapi import FastAPI
from database import Base, engine
from routers import foodstuff


app = FastAPI()
app.include_router(foodstuff.routers, prefix="/foodstuff")
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, workers=4)
