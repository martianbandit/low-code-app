from pydantic import BaseModel

class ApiKeyBase(BaseModel):
    name: str

class ApiKeyCreate(ApiKeyBase):
    key: str

class ApiKey(ApiKeyBase):
    id: int

    class Config:
        orm_mode = True
