from pydantic import BaseModel, ConfigDict


class Legislator(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class LegislatorVotes(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    legislator: str
    supported_bills: int
    opposed_bills: int
