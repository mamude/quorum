from app.domains.models import BillVotes
from app.services.csv_readers import get_data_bills_votes
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import UJSONResponse

router = APIRouter(
    prefix="/api/v1/bills",
    tags=["bills"],
    responses={404: {"description": "not found"}},
)


@router.get("/", response_model=BillVotes, response_class=UJSONResponse)
def get_bills():
    data = jsonable_encoder(get_data_bills_votes())
    return UJSONResponse(data)
