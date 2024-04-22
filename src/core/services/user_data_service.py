from core.repositories.user_data_repository import UserDataRepository, DeleteUser

async def delete_user_data(user_id):
    await UserDataRepository.delete_user(data=DeleteUser(user_id=user_id))