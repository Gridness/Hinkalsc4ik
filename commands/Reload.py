import os
import nextcord
from nextcord.ext import commands

from data.settings import GUILDS
from data.warningLevel import WARNING_LEVEL
from utils.log import log

class Reload(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    def setup(client):
        client.add_cog(Reload(client))

    @nextcord.slash_command(name='reload', guild_ids=[GUILDS], description='Reloads the bot')
    @commands.has_permissions(administrator=True)
    async def reload(self):
        log('Reloading extensions...', WARNING_LEVEL['medium'])
        try:
            for filename in os.listdir('./cogs'):
                if filename.endswith(".py"):
                    self.client.reload_extension(f'cogs.{filename[:-3]}')
        except Exception:
            log('An error occured while trying to reload extensions', WARNING_LEVEL['high'])
            raise Exception('Failed to reload extensions')

        log('Reload completed', WARNING_LEVEL['medium'])