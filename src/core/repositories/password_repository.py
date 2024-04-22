from core.models.pass_data_models import AddPassword, DeletePassword
from database.entities import new_session, Password
from sqlalchemy import select, update

class UserDataRepository:
    
    @staticmethod
    async def add_pass(cls, data: AddPassword):
        async with new_session() as session:
            dict = data.model_dump()

            pwd = Password(**dict)
            session.add(pwd)
            
            await session.commit()
    
    @staticmethod
    async def delete_pass(cls, data: DeletePassword):
        async with new_session() as session:
            query = update(Password).values(id=data.id).filter_by(id=data.id)

            result = await session.execute(query)
            await session.commit()
    
    @staticmethod
    async def get_pass_info(cls, data: DeletePassword):
        pass
    
    @staticmethod
    async def get_passwords(cls, data: DeletePassword):
        pass