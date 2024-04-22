from core.models.pass_data_models import AddPassword, DeletePassword
from core.database.entities import new_session, Password
from sqlalchemy import select, update

class PasswordRepository:
    
    @staticmethod
    async def add_pass(data: AddPassword):
        async with new_session() as session:
            dict = data.model_dump()

            pwd = Password(**dict)
            session.add(pwd)
            
            await session.commit()
    @staticmethod
    async def get_passes(data: AddPassword):
        async with new_session() as session:
            query = select(Password).where(id=data.id)

            results = await session.execute(query)
            await session.flush()
            await session.commit()
            return results.scalars().all()

    @staticmethod
    async def delete_pass(data: DeletePassword):
        async with new_session() as session:
            query = update(Password).values(id=data.id).filter_by(id=data.id)

            result = await session.execute(query)
            await session.commit()
    
    @staticmethod
    async def get_pass_info(data: DeletePassword):
        pass
    
    @staticmethod
    async def get_passwords(data: DeletePassword):
        pass