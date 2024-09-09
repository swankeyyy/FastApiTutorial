from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["items"])


@router.get('/{item_id}')
def get_by_id(item_id: Annotated[int, Path(ge=1, lt=4)]):
    return {"id": item_id}
