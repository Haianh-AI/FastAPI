from fastapi import APIRouter, Query
from services.transactions import get_transactions
from schemas.response import TransactionResponse

router = APIRouter()

@router.get("/transactions/", response_model=TransactionResponse)
def fetch_transactions(page: int = Query(1, description="Page number"), page_size: int = Query(10, description="Number of transactions per page")):
    return get_transactions(page, page_size)
