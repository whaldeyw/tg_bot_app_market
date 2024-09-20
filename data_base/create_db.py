import asyncio
import os
from sqlalchemy import String, BIGINT, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import select, update, delete
from config import ENGINE_DB


engin_db = os.getenv('ENGINE_DB')
engine = create_async_engine(ENGINE_DB, echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class Regs(Base):
    __tablename__ = 'registr'

    tg_id : Mapped[int] = mapped_column(BIGINT,primary_key=True)
    name : Mapped[str] = mapped_column(String(25))
    phone : Mapped[str] = mapped_column(String(25))

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    products = relationship('Product' , back_populates='category')

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[int]= mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    category = relationship('Category', back_populates='products')

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


#asyncio.run(async_main())



    