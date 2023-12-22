from pydantic import BaseModel


class MessageParams(BaseModel):
    model: str
    message: str
