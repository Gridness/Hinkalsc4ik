import nextcord
from nextcord.ext import commands

from data.settings import GUILDS

class Purge(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    def setup(client):
        client.add_cog(Purge(client))

    @nextcord.slash_command(name='purge', guild_ids=[GUILDS], description='Removes all roles from a user')
    @commands.has_permissions(administrator=True)
    async def purge(self, interaction: nextcord.Interaction):
        await interaction.response.send_message('NOT IMPLEMENTED YET')