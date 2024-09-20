
from aiogram import Router , F, Bot
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardButton

from kb import kb_reg



router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):

    await bot.send_message(message.from_user.id, f"Привет {message.from_user.username} Для того чтобы пользоваться нашим магазином пройди простую регистрацию\n"
                                                 ,  reply_markup=kb_reg)


