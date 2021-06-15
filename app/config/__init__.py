import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str
    RMQ_HOST: str
    RMQ_QUEUE: str

    class Config:
        env_file = "./config/environments/.env.local"


env_name = os.getenv("SERVICE_ENVIRONMENT")
settings = Settings(_env_file="./config/envs/.env.{}".format(env_name))
