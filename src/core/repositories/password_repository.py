from core.models.pass_data_models import AddPassword, DeletePassword, GetPassInfo, GetPasses, ChangePwdLogin, ChangePwdName, ChangePwdPassword
from core.database.entities import new_session, Password
from sqlalchemy import select, update, delete
from core.repositories.user_data_repository import UserDataRepository, GetUser
class PasswordRepository:
    
    @staticmethod
    async def add_pass(data: AddPassword):
        async with new_session() as session:
            dict = data.model_dump()

            pwd = Password(**dict)
            session.add(pwd)
            
            await session.commit()
    
    @staticmethod
    async def get_passes(data: GetPasses):
        async with new_session() as session:
            user = await UserDataRepository.get_user(GetUser(user_id=data.user_id))

            query = select(Password).filter_by(user_id=user.id)

            results = await session.execute(query)
            await session.flush()
            await session.commit()
            return results.scalars().all()

    @staticmethod
    async def delete_pass(data: DeletePassword):
        async with new_session() as session:
            query = delete(Password).filter_by(id=data.id)
            
            await session.execute(query)
            await session.commit()
    
    @staticmethod
    async def get_pass_info(data: GetPassInfo):
        async with new_session() as session:
            query = select(Password).filter_by(id=data.pass_id)
            
            result = await session.execute(query)
            pwd = result.scalar_one()
            await session.commit()
            return pwd
    @staticmethod
    async def change_pwd_pass(data: ChangePwdPassword):
        async with new_session() as session:
            query = select(Password).filter_by(id=data.pass_id)
            result = await session.execute(query)
            pwd = result.scalar_one()
            pwd.password = data.password
            session.add(pwd)
            await session.commit()
            
    @staticmethod
    async def change_pwd_name(data: ChangePwdName):
        async with new_session() as session:
            query = select(Password).filter_by(id=data.pass_id)
            result = await session.execute(query)
            pwd = result.scalar_one()
            pwd.name = data.name
            

            session.add(pwd)
            await session.commit()
    @staticmethod
    async def change_pwd_login(data: ChangePwdLogin):
        async with new_session() as session:
            query = select(Password).filter_by(id=data.pass_id)
            result = await session.execute(query)
            pwd = result.scalar_one()
            pwd.login = data.login
            session.add(pwd)
            await session.commit()