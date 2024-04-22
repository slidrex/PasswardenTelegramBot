from pydantic import BaseModel

class AddPassword(BaseModel):
    name: str
    login: str
    password: str
class DeletePassword(BaseModel):
    id: int