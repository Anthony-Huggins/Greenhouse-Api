from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class Location(BaseModel):
    """Pydantic class representing a single greenhouse
    
    Must have ONLY the follwing fields:
        id: int - The ID for the greenhouse in the database.
        location_ids: list[int] - List SQLite locationIDs
        name: str - The name of the greenhouse
        num_rows: int - how many rows for locations this greenhouse has (MAX - 6)
        locations_per_row: int - How many pots(locations) can fit in each row in this greenouse (MAX - 11)
        created_at: datetime - When this greenhouse was created
        updated_at: datetime - When this greenhouse was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(description="SQLite GreenhouseID")
    location_ids: list[int] = Field(description="List SQLite locationIDs")
    name: str = Field(max_length=25, description="Name of the greenhouse")
    num_rows: int = Field(gt=0, lt=6, description="how many rows are in the greenhouse")
    locations_per_row: int = Field(gt=0, lt=11, description="How many pots(locations) can fit in each row")
    created_at: datetime = Field(description="When this greenhouse was created")
    updated_at: datetime = Field(description="When this greenhouse was last updated")


  
