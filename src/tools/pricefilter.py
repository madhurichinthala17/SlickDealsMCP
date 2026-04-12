from src.Models.DataModel import PriceDetails
from typing import Optional


def filer_by_price(PriceDetails: PriceDetails, min_price: Optional[float] = None, max_price: Optional[float] = None) -> bool:
