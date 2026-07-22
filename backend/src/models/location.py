from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime


class Location(BaseModel):
    """Pydantic class representing a single location
    
    Must have ONLY the follwing fields:
        id: int - The ID for the plant in the database.
        plant_id: int - The ID for the plant in the database
        row_number: int - The row number the location is at in the greenhouse
        spot_number: int - The spot number the location is at withen the row
        created_at: datetime - When this care_log was created
        updated_at: datetime - When this care_log was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(description="SQLite Care_LogID")
    plant_id: int | None = Field(default=None, description="SQLite plant id")
    row_number: int = Field(description="The row number the location is at in the greenhouse")
    spot_number: int = Field(description="the spot number the location is at withen the row")
    created_at: datetime = Field(description="When this care_log was created")
    updated_at: datetime = Field(description="When this care_log was last updated")
  
