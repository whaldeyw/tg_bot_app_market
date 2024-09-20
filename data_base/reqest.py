import asyncio
from create_db import  async_main



def start():
    asyncio.run(async_main())

start()