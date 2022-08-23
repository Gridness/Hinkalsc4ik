from nextcord.ext import commands
from data.settings import CHANNEL_ID, EMBED_COLOR

from utils.buildEmbed import build_embed
from utils.log import log
from views.RoleView import RoleView

class Join(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log(f'{member} has joined the server for the first time or he has just rejoined')
        channel = self.client.get_channel(CHANNEL_ID)
        await channel.send(embed=build_embed(self.client, '', f'{member.mention}', EMBED_COLOR, False, hasImage=True, imageUrl=''),
        view=RoleView(self.client))

def setup(client):
    client.add_cog(Join(client))
