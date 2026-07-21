from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime


class Location(BaseModel):
    """Pydantic class representing a single greenhouse
    
    Must have ONLY the follwing fields:
        id: int - The ID for the greenhouse in the database.
        name: str - The name of the greenhouse
        num_rows: int - how many rows for locations this greenhouse has
        locations_per_row: int - How many pots(locations) can fit in each row in this greenouse
        created_at: datetime - When this greenhouse was created
        updated_at: datetime - When this greenhouse was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(description="SQLite Care_LogID")
    name: str = Field(max_length=25, description="Name of the warehouse")
    num_rows: int = Field(gt=0, lt=6, description="how many rows are in the greenhouse")
    locations_per_row: int = Field(gt=0, lt=11, description="How many pots(locations) can fit in each row")
    created_at: datetime = Field(description="When this care_log was created")
    updated_at: datetime = Field(description="When this care_log was last updated")


  
