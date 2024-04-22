from core.models.user_data_models import DeleteUser, AddUser
from database.entities import new_session, User
from sqlalchemy import select, update, values, filter

class UserDataRepository:
    @classmethod
    async def add_user(cls, data: AddUser):
        async with new_session() as session:
            dict = data.model_dump()

            user = User(**dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.user_id

    @classmethod
    async def delete_user(cls, data: DeleteUser):
        async with new_session() as session:
            query = update(User).values(user_id=data.user_id).filter_by(user_id=data.user_id)

            result = await session.execute(query)
            await session.commit()