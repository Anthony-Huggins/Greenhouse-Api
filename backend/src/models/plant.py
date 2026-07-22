from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Literal


Status = Literal["thriving", "stable", "struggling", "dormant", "dead"]

class Plant(BaseModel):
    """Pydantic class representing a single plant that is planted in the greenhouse
    
    Must have ONLY the follwing fields:
        id: int - The ID for the plant in the database.
        species_id: int - The id of the species that the plant is 
        nickname: str - Plant's Nickname
        pot_size: int - Size of the pot in cm
        acquisiton_date: datetime - When this plant was aquired
        health_status: str - The health status of a plant. Can be: ['thriving', 'stable', 'struggling', 'dormant', 'dead']"
        created_at: datetime - When this plant was regested in the system
        updated_at: datetime - When this plant was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(description="SQLite SpeciesID")
    species_id: int = Field(description="SQLite PlantID")
    nickname: str = Field(default="", max_length=50, min_length="1")
    pot_size: int | None = Field(default=None, description="Pot size in cm")
    acquisiton_date: datetime = Field(description="When this plant was aquired")
    health_status: Status = Field(default="stable", description="The health status of a plant. Can be: 'thriving', 'stable', 'struggling', 'dormant', 'dead'")
    created_at: datetime = Field(description="When this plant was regested in the system")
    updated_at: datetime = Field(description="When this plant was last updated")
  
