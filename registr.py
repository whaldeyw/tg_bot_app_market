from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import  F, Router
from aiogram.types import Message
from sqlalchemy import select, update, delete
from data_base.create_db import Regs, async_session, engine
import asyncio

from kb import del_kb_reg

reg_router = Router()
class RegState(StatesGroup):
    regName = State()
    regAdress = State()


async def get_user():
    async with async_session() as session:
        @reg_router.message(StateFilter(None), F.text == 'Регистрация')
        async def add_name(message:Message, state: FSMContext):
            users_id = await session.scalars(select(Regs))
            us = ([i.tg_id for i in users_id])
            if message.from_user.id in us:
                await message.answer(f'Вы уже зарегистрированы! Добро пожаловать в магазин', reply_markup=del_kb_reg)
                await state.clear()

            else:

                await message.answer(f'для начала давайте познакомимся!😉 \nКак тебя зовут? ', reply_markup=del_kb_reg)
                await state.set_state(RegState.regName)
                await del_kb_reg

asyncio.run(get_user())

@reg_router.message(RegState.regName, F.text )
async def add_adress(message:Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите ваш номер телефона')
    await state.set_state(RegState.regAdress)


async def set_user():
    async with async_session() as session:
        @reg_router.message(RegState.regAdress, F.text )
        async def add_adress(message:Message, state: FSMContext):
            await state.update_data(phone=message.text)
            await message.answer('Регистрация прошла успешно!')
            data = await state.get_data()
            await message.answer(f'Добро пожаловать {data["name"]}  \nВаш номер телефона {data["phone"]}')
            await state.clear()

            tg_id = message.from_user.id
            session.add(Regs(tg_id= tg_id, name=f'{data["name"]}', phone=f'{data["phone"]}'))
            await session.commit()

asyncio.run(set_user())

