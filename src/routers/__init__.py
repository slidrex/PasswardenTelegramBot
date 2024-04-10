from aiogram import Router

from .main_menu_router import rt as main_router


router = Router()

router.include_router(
    main_router
)