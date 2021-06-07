from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str


def user_dict(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "token": user["token"],
        "created_at": user["created_at"],
    }
