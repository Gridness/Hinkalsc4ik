import os
import nextcord
from nextcord.ext import commands

from data.settings import SERVER_ID
from data.warningLevel import WARNING_LEVEL
from utils.loadExtensions import loadExtensions
from utils.log import log

class Reload(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        
    server_id = SERVER_ID

    @nextcord.slash_command(name='reload', guild_ids=[server_id], description='Reloads the bot')
    async def reload(self):
        log('Reloading extensions...', WARNING_LEVEL['medium'])

        loadExtensions(self.client, 'cogs', './cogs', 'reload')
        loadExtensions(self.client, 'commands', './commands', 'reload')
        
        # try:
        #     for filename in os.listdir('./cogs'):
        #         if filename.endswith(".py"):
        #             self.client.reload_extension(f'cogs.{filename[:-3]}')
        # except Exception:
        #     log('An error occured while trying to reload extensions', WARNING_LEVEL['high'])
        #     raise Exception('Failed to reload extensions')
 
        # try:
        #     for filename in os.listdir('./commands'):
        #         if filename.endswith(".py"):
        #             self.client.reload_extension(f'commands.{filename[:-3]}')
        # except Exception:
        #     log('An error occured while loading extensions', WARNING_LEVEL['high'])
        #     raise Exception('Failed to reload extensions')

        log('Reload completed', WARNING_LEVEL['medium'])

def setup(client):
    client.add_cog(Reload(client))