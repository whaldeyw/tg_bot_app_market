from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import  F, Router
from aiogram.types import Message
from sqlalchemy import select, update, delete
from data_base.create_db import Regs, async_session, Category
import asyncio



add_category_router = Router()
class AddCategoryState(StatesGroup):
    addCategory = State()


@add_category_router.message(StateFilter(None), F.text == 'Добавить категорию')
async def add_names(message:Message, state: FSMContext):
    await message.answer(f'Введите название категории ')
    await state.set_state(AddCategoryState.addCategory)


async def set_category():
    async with async_session() as session:
        @add_category_router.message(AddCategoryState.addCategory, F.text )
        async def add_end(message:Message, state: FSMContext):
            await state.update_data(category=message.text)
            data = await state.get_data()
            await message.answer(f'Категория добавлена успешно {data["category"]} ')
            await state.clear()

            session.add(Category(name=f'{data["category"]}'))
            await session.commit()
asyncio.run(set_category())