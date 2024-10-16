import asyncio
from concurrent.futures import ThreadPoolExecutor

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import UserRepository
from database import get_async_session
from logs.models import LogsRepository
from logs.utils import add_log
from post_router.utils import get_weather_data
from base_config import Settings

router = APIRouter(
    prefix="/get_weather",
    tags=["Weather"]
)


@router.post("/get_weather_by_id")
async def get_weather_by_id(user_tg_id: int, city: str, session: AsyncSession = Depends(get_async_session)):
    """
    По telegram id пользователя бота и городу получить данные о погоде \n
    Возвращает обьект dict вида: \n

        some_dict =
            {
              "town": "Лондон",
              "temperature": 15.04,
              "feels_like": 14.74,
              "weather_description": "пасмурно",
              "humidity": 82,
              "wind_speed": 1.54
            }
    """
    logs_repo = LogsRepository()
    user_repo = UserRepository()
    api_key = Settings().get_api_key()
    res = await asyncio.to_thread(get_weather_data, city, api_key)
    field_filter = {
        "tg_user_id": user_tg_id
    }
    user = await user_repo.get_one_by_fields(session=session, data=["id", "tg_user_id"], field_filter=field_filter)
    if not user:
        return HTTPException(status_code=400, detail={"Пользователь не найден"})
    if not res:
        await add_log(session=session, repo=logs_repo, tg_user_id=user_tg_id,
                      request=f"get_weather_by_id user:{user_tg_id} city:{city}", status="City Not Found")
        return HTTPException(status_code=400, detail={"Город не найден или ошибка на строне openweather"})
    else:
        await add_log(session=session, repo=logs_repo, tg_user_id=user_tg_id,
                      request=f"get_weather_by_id user:{user_tg_id} city:{city}", status="OK")
        return res

