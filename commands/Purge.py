import nextcord
from nextcord.ext import commands

from data.settings import EMBED_COLOR, SERVER_ID
from utils.buildEmbed import build_embed
from utils.log import log

class Purge(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    server_id = SERVER_ID

    @nextcord.slash_command(name='purge', guild_ids=[server_id], description='Removes all roles from a user')
    async def purge(self, member: nextcord.Member):
        await member.remove_roles()
        await member.send(embed=build_embed(self.client, 'НАКОЛОЧКИ, НАКОЛОЧКИ', 'ГОП, ТАТУИРОВОЧКИ', EMBED_COLOR, False))
        log(f'{member} has lost all his roles. Oh no')

def setup(client):
    client.add_cog(Purge(client))