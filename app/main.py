from fastapi import FastAPI, status, Depends, HTTPException
from uuid import UUID

from .Exeptions import TaskNotFoundError
from .schemas.task import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from .servicies.task import TaskService
from .dependicies import get_task_service


app = FastAPI()

@app.get("/tasks", response_model=list[TaskSchema])
async def get_tasks(service: TaskService = Depends(get_task_service)) -> list[TaskSchema]:
    return await service.list_of_tasks()

@app.post("/tasks", response_model=TaskSchema)
async def create_task(payload: TaskCreateSchema, service: TaskService = Depends(get_task_service)) -> TaskSchema:
    return await service.create_task(payload)

@app.patch("/tasks/{id}", response_model=TaskSchema)
async def update_task(task_id: UUID, payload: TaskUpdateSchema, service: TaskService = Depends(get_task_service)) -> TaskSchema:
    try:
        return await service.update_task(task_id, payload)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        )

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID, service: TaskService = Depends(get_task_service)) -> None:
    try:
        await service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
        )

