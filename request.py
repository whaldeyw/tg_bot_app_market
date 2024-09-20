import asyncio

from data_base.create_db import Regs, async_session, Category, Product
from sqlalchemy import select

async def get_categories():
    async with async_session() as session:
        category = await session.scalars(select(Category))
        result = ([i.name for i in category])
        return result
