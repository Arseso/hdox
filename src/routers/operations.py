from fastapi import APIRouter

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get('/search/{search_request}')
async def search(search_request: str):
    # Search by request 
    raise NotImplementedError
