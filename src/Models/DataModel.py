from datetime import datetime
from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Item(BaseModel):
    title: str
    link: HttpUrl
    current_price: Optional[float] | str= None
    original_price: Optional[float] | str = None
    discount_percentage: Optional[float]  | str = None
    posted_details: Optional[str]  | str = None

class SearchDealsOutput(BaseModel):
    result: List[Item]
    total: int

class PriceDetails(BaseModel):
    current_price: Optional[float] | str = None
    original_price: Optional[float] | str = None
    discount_percentage: Optional[float] | str = None

class RecentItem(BaseModel):
    title: str
    link: HttpUrl
    posted_date : Optional[datetime] = None