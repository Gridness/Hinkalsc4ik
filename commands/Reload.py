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

    @nextcord.slash_command(name='reload', description='Reloads the bot', guild_ids=[server_id])
    async def reload(self):
        log('Reloading extensions...', WARNING_LEVEL['medium'])

        loadExtensions(self.client, 'cogs', './cogs', 'reload')
        loadExtensions(self.client, 'commands', './commands', 'reload')

        log('Reload completed', WARNING_LEVEL['medium'])

def setup(client):
    client.add_cog(Reload(client))