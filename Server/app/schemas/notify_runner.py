from pydantic import BaseModel


class NotifyRunnerBase(BaseModel):
    endpoint: str | None = None


class NotifyRunnerCreate(NotifyRunnerBase):
    endpoint: str
    username: str


class NotifyRunnerInDBBase(NotifyRunnerBase):
    id: int

    class Config:
        orm_mode = True


class NotifyRunner(NotifyRunnerInDBBase):
    pass
