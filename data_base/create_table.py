import os

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from create_db import Regs, Category
import asyncio
import asyncpg
from config import ENGINE_DB


engine = create_async_engine(ENGINE_DB, echo=True)

async_session = async_sessionmaker(engine)

async def set_user():
    async with async_session() as session:
        session.add(Regs(tg_id= 9999113432, name='OlegS', phone='fdsfdsfSSsd'))
        await session.commit()

async def sets_user():
    async with async_session() as session:
        session.add(Category(id= 9933331, name='ghgheg'))
        await session.commit()

async def get_user():
    async with async_session() as session:
        # user = await session.scalar(select(User).where(User.name=='More'))
        # print(user.name)
        users_id = await session.scalars(select(Regs))
        us = ([i.tg_id for i in users_id])
        if 12313872132 in us:
            print('Ok')
        else:
            print('now')

async def gets_user():
    async with async_session() as session:
        # user = await session.scalar(select(User).where(User.name=='More'))
        # print(user.name)
        users_id = await session.scalars(select(Category))
        us = ([i.name for i in users_id])
        print(us)
