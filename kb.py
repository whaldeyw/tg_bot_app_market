
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



kb_reg = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Регистрация')],
], resize_keyboard=True, input_field_placeholder='Для продолжения жми ниже')

del_kb_reg = ReplyKeyboardRemove()


