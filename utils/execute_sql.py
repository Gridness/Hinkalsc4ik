import os

from data.warningLevel import WARNING_LEVEL
from data.settings import DEFAULT_RELATIVE_DB_PATH
from data.config.config import CONFIG
from utils.log import log

try:
    import aiosqlite
except ImportError:
    os.system('pip install -U aiosqlite')
    import aiosqlite

async def execute_sql(query):
    async with aiosqlite.connect(DEFAULT_RELATIVE_DB_PATH) as db:
        async with db.cursor() as cursor:
            await cursor.execute(query)
        await db.commit()

        if CONFIG["logging"]["displayQueries"]:
            log(f'Successfully executed query {query}', WARNING_LEVEL['medium'])