from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.logs.models import LogsRepository

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


@router.get("/{user_id}")
async def get_logs_by_id(user_id: int, session: AsyncSession = Depends(get_async_session)):
    logs_repo = LogsRepository()
    field_filter = {
        "user_tg_id": user_id
    }
    res = await logs_repo.get_all_by_fields(session=session, data=["user_tg_id", "request", "registered_at"],
                                            field_filter=field_filter)
    return res


@router.get("")
async def get_logs_by_id(session: AsyncSession = Depends(get_async_session)):
    logs_repo = LogsRepository()
    res = await logs_repo.get_all_by_fields(session=session, data=["user_tg_id", "request", "registered_at"])
    return res
