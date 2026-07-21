from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime




class Species(BaseModel):
    """Pydantic class representing a single species of plant 
    that we grow in our greenhouse.
    
    Must have ONLY and the follwing fields:
        id: int - The ID for the species in the database.
        name: str - The offical name of the species
        common_name: str - Common name (what people call it not the offical species name)
        sunlight_target: int - How much sunlight a species needs per day in DLI (total amount of photosynthetically active radiation (PAR) a plant receives over a 24-hour period.)
        watering_interval_target: int - How many times a plant needs to be wattered in a day
        created_at: datetime - When this species record was created
        updated_at: datetime - When this species record was last updated
    """

    model_config = ConfigDict(extra="forbid")


    id: int = Field(default=None, gt=0, description="SQLite SpeciesID")
    name: str = Field(max_length=50, description="Name of the species")
    common_name: str = Field(max_length=25, description="Common name (what people call it not the offical species name)")
    sunlight_target: int = Field(gt=0, lt=61, description="How much sunlight a species needs per day in DLI")
    watering_interval_target: int = Field(gt=0, lt=11, description="How often this species needs to be wattered per day")
    created_at: datetime
    updated_at: datetime