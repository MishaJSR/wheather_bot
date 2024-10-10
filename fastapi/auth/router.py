import os

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import UserRepository
from auth.schemas import ConstructUser
from database import get_async_session
from logs.models import LogsRepository
from logs.utils import add_log

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/check_or_create")
async def create_user(tg_user_id: int, user_tag: str = "@", session: AsyncSession = Depends(get_async_session)):
    """
    Создать пользователя, если он уже есть в базе вернуть его структуру \n
    Для первого случая возвращается id в таблице users\n
    Для второго случая возвращается обьект dict вида\n
        some_dict =
            {
                "id": 4,
                "tg_user_id": 123123
            }

    """
    user_repo = UserRepository()
    logs_repo = LogsRepository()
    field_filter = {
        "tg_user_id": tg_user_id
    }
    res = await user_repo.get_one_by_fields(session=session, data=["id", "tg_user_id"], field_filter=field_filter)
    if res:
        await add_log(session=session, repo=logs_repo, tg_user_id=tg_user_id,
                      request=f"User {tg_user_id} already add", status="OK")
        return res
    else:
        res = await user_repo.add_object(session=session, data=ConstructUser(tg_user_id=tg_user_id,
                                                                             user_tag=user_tag).model_dump())
        await add_log(session=session, repo=logs_repo, tg_user_id=tg_user_id,
                      request=f"Add new user {tg_user_id}", status="OK")
        return res
