from pydantic import BaseModel, ConfigDict
from uuid import UUID


class TaskSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    text: str
    done: bool = False


class TaskUpdateSchema(BaseModel):
    text: str | None = None
    done: bool | None = None


class TaskCreateSchema(BaseModel):
    text: str