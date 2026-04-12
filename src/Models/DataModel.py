from pydantic import BaseModel,HttpUrl
from typing import List, Optional

class Item(BaseModel):
    title: str
    link: HttpUrl
    price: Optional[float] = None

class SearchDealsOutput(BaseModel):
    result: List[Item]
    total: int

class PriceDetails(BaseModel):
    current_price: float
    original_price: float
    discount_percentage: float