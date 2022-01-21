from pydantic import BaseModel


class Response(BaseModel):
    daily: str
    weekly: str
    monthly: str
    yearly: str
