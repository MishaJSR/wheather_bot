from typing import Optional, Union

from pydantic import BaseModel, conint


class ConstructUser(BaseModel):
    tg_user_id: conint(strict=True, gt=0)
    user_tag: Optional[str] = "@"

