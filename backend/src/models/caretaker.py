from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime
from typing import Literal

class Caretaker(BaseModel):
    """Pydantic class representing a single caretaker that works at the greenhouse
    
    Must have ONLY the follwing fields:
        id: int - The ID for the plant in the database.
        first_name: str - Caretakers First name
        last_name: str - Caretakers Last name
        email: str - Caretakers email
        phone_number - Caretakers phone number
        created_at: datetime - When this caretaker was regested in the system
        updated_at: datetime - When this caretaker was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(description="SQLite CaretakerID")
    first_name: str = Field(max_length=50, description="Caretakers first name")
    last_name: str = Field(max_length=50, description="Caretakers Last name")
    email: EmailStr = Field(description="Caretakers Email")
    phone_number: str = Field(pattern=r"^\d{10}$", description="Caretakers phone number")
    created_at: datetime = Field(description="When this caretaker was regested in the system")
    updated_at: datetime = Field(description="When this caretaker was last updated")
  
