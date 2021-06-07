from fastapi import FastAPI
import uvicorn
from api.routes import router
from repositories.db_manager import connect_to_mongo, close_mongo_connection

app = FastAPI()

app.include_router(router, prefix='/api')


app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
