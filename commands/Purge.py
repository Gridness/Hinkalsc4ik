import nextcord
from nextcord.ext import commands

from data.settings import EMBED_COLOR, GUILDS
from utils.buildEmbed import build_embed

class Purge(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    def setup(client):
        client.add_cog(Purge(client))

    @nextcord.slash_command(name='purge', guild_ids=[GUILDS], description='Removes all roles from a user')
    @commands.has_permissions(administrator=True)
    async def purge(self, member: nextcord.Member):
        await member.remove_roles()
        await member.send(embed=build_embed(self.client, 'НАКОЛОЧКИ, НАКОЛОЧКИ', 'ГОП, ТАТУИРОВОЧКИ', EMBED_COLOR, False))