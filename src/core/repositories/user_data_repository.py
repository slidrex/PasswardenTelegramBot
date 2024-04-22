from core.models.user_data_models import DeleteUser, AddUser, GetUser
from core.database.entities import new_session, User, DeleteDataHistory
from sqlalchemy import update, select
import datetime

class UserDataRepository:
    @classmethod
    async def add_user(cls, data: AddUser):
        async with new_session() as session:
            dict = data.model_dump()

            user = User(**dict)
            user.is_deleted = False

            session.add(user)
            await session.commit()
    @classmethod
    async def get_user(cls, data: GetUser) -> User:
        async with new_session() as session:
            query = select(User).filter_by(user_id=data.user_id)

            result = await session.execute(query)
            await session.flush()
            return result.scalar()

        
    @classmethod
    async def delete_user(cls, data: DeleteUser):
        async with new_session() as session:

            history_item = DeleteDataHistory()
            history_item.user_id = data.user_id
            history_item.delete_time = datetime.datetime.now()

            session.add(history_item)
            await session.commit()