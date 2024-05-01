from app.domains.models import Legislator
from app.services.csv_readers import get_data_legislators_votes
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import UJSONResponse

router = APIRouter(
    prefix="/api/v2/legislators",
    tags=["legislators"],
    responses={404: {"description": "not found"}},
)


@router.get("/", response_model=Legislator, response_class=UJSONResponse)
def get_legislators():
    data = jsonable_encoder(get_data_legislators_votes())
    return UJSONResponse(data)
