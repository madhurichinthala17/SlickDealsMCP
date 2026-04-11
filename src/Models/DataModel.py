from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    title: str
    link: str
    price: Optional[float] = None