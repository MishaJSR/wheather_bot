from typing import Optional

from pydantic import BaseModel, conint


class ConstructLog(BaseModel):
    user_tg_id: conint(strict=True, gt=0)
    request: str
    status: str
