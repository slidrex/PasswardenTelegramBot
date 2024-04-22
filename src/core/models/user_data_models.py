from pydantic import BaseModel

class DeleteUser(BaseModel):
    user_id: int
class AddUser(BaseModel):
    user_id: int
class GetUser(BaseModel):
    user_id: int