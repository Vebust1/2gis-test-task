from pydantic import BaseModel, Field
from typing import Optional

class FavoritePlace(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=999)
    lat: float
    lon: float
    color: Optional[str] = None
    created_at: str