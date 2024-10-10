from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.logs.models import LogsRepository

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)

# Модель данных для элемента
class Item(BaseModel):
    id: int
    name: str

# Временное хранилище для элементов

@router.get("/{user_id}")
async def get_logs_by_id(user_id: int, skip: int = Query(0, ge=0), limit: int = Query(10, gt=0),
                         session: AsyncSession = Depends(get_async_session)):
    """
    По telegram id пользователя \n
    Возвращает обьект вида: \n

        some_list =
            [
              {
                "user_tg_id": 123123,
                "request": "Add new user 123123",
                "registered_at": "2024-10-09T09:43:00.017953"
              },
              {
                "user_tg_id": 123123,
                "request": "get_weather_by_id user:123123 city:Kdfsfsdfsf",
                "registered_at": "2024-10-09T10:36:01.639712"
              },
              {
                "user_tg_id": 123123,
                "request": "get_weather_by_id user:123123 city:Лондон",
                "registered_at": "2024-10-09T10:36:07.006732"
              },
            ]
    """
    logs_repo = LogsRepository()
    field_filter = {
        "user_tg_id": user_id
    }
    res = await logs_repo.get_all_by_limits(session=session, data=["user_tg_id", "request", "registered_at"],
                                            field_filter=field_filter, limit=limit, skip=skip)
    return res


@router.get("")
async def get_all_logs(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0),
                       session: AsyncSession = Depends(get_async_session)):
    """
    Возвращает все логи в обьекте вида: \n

        some_list =
            [
              {
                "user_tg_id": 123123,
                "request": "Add new user 123123",
                "registered_at": "2024-10-09T09:43:00.017953"
              },
              {
                "user_tg_id": 123123,
                "request": "get_weather_by_id user:123123 city:Kdfsfsdfsf",
                "registered_at": "2024-10-09T10:36:01.639712"
              },
              {
                "user_tg_id": 123123,
                "request": "get_weather_by_id user:123123 city:Лондон",
                "registered_at": "2024-10-09T10:36:07.006732"
              },
            ]
    """
    logs_repo = LogsRepository()
    res = await logs_repo.get_all_by_limits(session=session, data=["user_tg_id", "request", "registered_at"],
                                            limit=limit, skip=skip)
    return res
