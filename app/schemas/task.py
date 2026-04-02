from pydantic import BaseModel
from uuid import UUID


class TaskSchema(BaseModel):
    id: UUID
    text: str
    done: bool = False


class TaskUpdateSchema(BaseModel):
    text: str | None = None
    done: bool | None = None


class TaskCreateSchema(BaseModel):
    text: str