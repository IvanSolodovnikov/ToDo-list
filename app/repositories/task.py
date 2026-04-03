from typing import Sequence, Any
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.task import TaskORM


class TaskRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_task(self, text: str) -> TaskORM:
        task = TaskORM(text=text)
        self.db.add(task)
        return task

    async def get_all(self) -> list[TaskORM] | Sequence[Any]:
        result = await self.db.execute(select(TaskORM))
        tasks = result.scalars().all()
        return tasks

    async def get_by_id(self, task_id: UUID) -> TaskORM | None:
        return await self.db.get(TaskORM, task_id)

    async def delete_task(self, task: TaskORM) -> None:
        await self.db.delete(task)
