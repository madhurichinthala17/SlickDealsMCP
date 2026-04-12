from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Item(BaseModel):
    title: str
    link: HttpUrl
    price: Optional[float] = None
    current_price: Optional[float] = None
    original_price: Optional[float] = None
    discount_percentage: Optional[int] = None
    posted_details: Optional[str] = None

class SearchDealsOutput(BaseModel):
    result: List[Item]
    total: int

class PriceDetails(BaseModel):
    current_price: Optional[float] = None
    original_price: Optional[float] = None
    discount_percentage: Optional[int] = None