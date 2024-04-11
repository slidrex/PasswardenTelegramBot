from aiogram import Router
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram_dialog.widgets.kbd import Checkbox, ManagedCheckbox
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import DialogManager, ChatEvent


rt = Router(name=__name__)

class AddPassword(StatesGroup):
    input_pass= State()
    input_name=State()
    input_login=State()

async def check_changed(event: ChatEvent, checkbox: ManagedCheckbox,
                        manager: DialogManager):
    print("Check status changed:", checkbox.is_checked())

@rt.message(AddPassword.input_name)
async def input_name_async(message: Message, state: FSMContext):
    
    await message.answer(text=f'Введите логин')
    await state.update_data(input_name=message.text)
    await state.set_state(AddPassword.input_login)

@rt.message(AddPassword.input_login)
async def input_login_async(message: Message, state: FSMContext):
    
    
    
    builder = InlineKeyboardBuilder()
    builder.button(text="Ввести вручную", callback_data="manual_pass")
    builder.button(text="Сгенерировать", callback_data="generate_pass")
    
    

    builder.adjust(1, 1)
    await message.answer(text=f'Выберите способ создания пароля:', reply_markup=builder.as_markup())
    
    await state.update_data(input_login=message.text)
    await state.set_state(AddPassword.input_pass)

@rt.message(AddPassword.input_pass)
async def input_pass_async(message: Message, state: FSMContext):
    await state.update_data(input_pass=message.text)
    data = await state.get_data()
    await message.answer(text=[data["input_name"], data["input_login"],data["input_pass"]])

@rt.callback_query(F.data == "generate_pass")
async def input_pass_async(callback_query: CallbackQuery, state: FSMContext):
    builder = InlineKeyboardBuilder()
    

    builder.button(text="Применить", callback_data="sss")
    #🟢🔴
    additional_symbol = "🟢"
    
    #if "include_symbols" in data.keys() and data["include_symbols"] == False:
    additional_symbol = "🔴"
            
    #builder.button(text="Спецсимволы " + additional_symbol, callback_data="check_symbols")
    check = Checkbox(
    Const("✓  Checked"),
    Const("Unchecked"),
    id="include_symbols",
    default=True,  # so it will be checked by default,
    on_state_changed=check_changed,
)
    
    builder.button(text="Изменить длину", callback_data="sss")
    builder.button(text="Сгенерировать новый", callback_data="sss")
    builder.button(text="⬅️ Назад", callback_data="sss")
    builder.button(text="❌ Закрыть", callback_data="sss")
    builder.adjust(1, 2, 1, 2)
    await callback_query.message.edit_text(text="`password`", reply_markup= builder.as_markup(), parse_mode='MarkdownV2')
