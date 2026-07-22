from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime
from typing import Literal
from models import Status

Care_Types = Literal["watered", "fertilized", "repotted", "pruned", "pest_treatment", "observation"]

class Care_Log(BaseModel):
    """Pydantic class representing a single care log
    
    Must have ONLY the follwing fields:
        id: int - The ID for the plant in the database.
        caretaker_id: int - The id of the caretaker that did this care_log 
        care_type: str - type of care. options: ['watered', 'fertilized', 'repotted', 'pruned', 'pest_treatment', 'observation']
        notes: list[str] - Any aditional notes the caretaker has
        date_of_care: datetime - When the care happened (editable)
        created_at: datetime - When this care_log was created
        updated_at: datetime - When this care_log was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(description="SQLite Care_LogID")
    caretaker_id: int = Field(description="SQLite caretaker ID")
    plant_id: int = Field(description="SQLite plantID")
    care_type: Care_Types = Field(description="type of care. options: 'watered', 'fertilized', 'repotted', 'pruned', 'pest_treatment', 'observation'")
    notes: list[str] = Field(default="", description="Notes for this care log")
    date_of_care: datetime = Field(description="When the care happened (editable)")
    created_at: datetime = Field(description="When this care_log was created")
    updated_at: datetime = Field(description="When this care_log was last updated")
  
