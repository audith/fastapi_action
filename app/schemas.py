from pydantic import BaseModel

class Usercreate(BaseModel):
    name:str



class UserResponse(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes=True
    