from pydantic import BaseModel

class AddPassword(BaseModel):
    user_id: int
    name: str
    login: str
    password: str
class DeletePassword(BaseModel):
    user_id: int