import logging
import datetime
from nextcord.ext import commands

from cogs.Ping import Ping
from cogs.Phrases import Phrases
from data.meta import META
from data.warningLevel import WARNING_LEVEL
from utils.cls import cls
from utils.log import log
from utils.execute_sql import execute_sql
from views.RoleView import RoleView

class Ready(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        now = datetime.datetime.now()

        cls()
        
        logger = logging.getLogger('nextcord')
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='nextcord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

        execute_sql('CREATE TABLE IF NOT EXISTS jokes (jokeID INTEGER, joke TEXT, PRIMARY KEY("jokeID" AUTOINCREMENT))')
        execute_sql('CREATE TABLE IF NOT EXISTS statuses (statusID INTEGER, status TEXT, PRIMARY KEY("statusID" AUTOINCREMENT))')

        if now.year == 2022:
            log(f'{META["name"]} {META["ver"]} (c) {META["dev"]} 2022', WARNING_LEVEL['medium'], logType='print')
        else:
            log(f'{META["name"]} {META["ver"]} (c) {META["dev"]} 2022 - {now.year}', WARNING_LEVEL['medium'], logType='print')

        log(f'This software is licensed under the {META["license"]} license. All rights reserved', WARNING_LEVEL['medium'], logType='print')

        self.client.add_view(RoleView(self.client))

        Ping.getPing.start(self)
        Phrases.changePresence.start(self)
   
        log(f'{self.client.user} is online')

def setup(client):
    client.add_cog(Ready(client))