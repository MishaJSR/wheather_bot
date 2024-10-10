from datetime import datetime
from sqlalchemy import (TIMESTAMP, Boolean, Column, Integer, String, ForeignKey, BigInteger)

from src.database import Base
from src.repository.repository import SQLAlchemyRepository


class Logs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    user_tg_id = Column(BigInteger, ForeignKey('user.tg_user_id'))
    request = Column(String, nullable=False)
    status = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)


class LogsRepository(SQLAlchemyRepository):
    model = Logs
