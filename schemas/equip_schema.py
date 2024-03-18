from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    quantity: int


class UpdateBase(BaseModel):
    quantity: int
