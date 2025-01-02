from pydantic import BaseModel

class UserBase(BaseModel):
    username:str
    password:str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id:int

    class Config:
        from_attributes=True

class TodoBase(BaseModel):
    title:str
    description:str|None=None
    completed:bool=False

class TodoCreate(TodoBase):
    pass
class TodoResponse(TodoBase):
    id:int

    class Config:
        from_attributes=True
