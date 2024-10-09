from src.logs.schemas import ConstructLog


async def add_log(session, repo, tg_user_id, request, status):
    _ = await repo.add_object(session=session, data=ConstructLog(user_tg_id=tg_user_id,
                                                                 request=request,
                                                                 status=status).model_dump())
