from pydantic import BaseModel


class Notification(BaseModel):
    providers: set
    body: str
    receivers: set


def notification_dict(notification) -> dict:
    return {
        "id": str(notification["_id"]),
        "providers": notification["providers"],
        "receivers": notification["receivers"],
        "body": notification["body"],
        "created_at": notification["created_at"],
    }
