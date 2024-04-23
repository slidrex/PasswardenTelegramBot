from pydantic import BaseModel

class AddPassword(BaseModel):
    user_id: int
    name: str
    login: str
    password: str
class DeletePassword(BaseModel):
    id: int
class GetPassInfo(BaseModel):
    pass_id: int
class GetPasses(BaseModel):
    user_id: int
class ChangePwdPassword(BaseModel):
    pass_id: int
    password: str
class ChangePwdLogin(BaseModel):
    pass_id: int
    login: str
class ChangePwdName(BaseModel):
    pass_id: int
    name: str