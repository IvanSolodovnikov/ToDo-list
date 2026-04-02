from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .servicies.task import TaskService
from .database.db import get_db


def get_task_service(db: AsyncSession = Depends(get_db)) -> TaskService:
    return TaskService(db=db)