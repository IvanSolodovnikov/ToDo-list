from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.Exeptions import TaskNotFoundError
from app.repositories.task import TaskRepository
from app.schemas.task import TaskSchema, TaskCreateSchema, TaskUpdateSchema



class TaskService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = TaskRepository(db)

    async def list_of_tasks(self) -> list[TaskSchema]:
        tasks = await self.repository.get_all()
        return [TaskSchema.model_validate(task) for task in tasks]

    async def create_task(self, payload: TaskCreateSchema) -> TaskSchema:
        task = await self.repository.create_task(text=payload.text)
        await self.db.commit()
        await self.db.refresh(task)
        return TaskSchema.model_validate(task)

    async def update_task(self, task_id: UUID, payload: TaskUpdateSchema) -> TaskSchema:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError
        if payload.text:
            task.text = payload.text
        if payload.done is not None:
            task.done = payload.done
        await self.db.commit()
        await self.db.refresh(task)
        return TaskSchema.model_validate(task)

    async def delete_task(self, task_id: UUID) -> None:
        task = await self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundError
        await self.repository.delete_task(task)
        await self.db.commit()