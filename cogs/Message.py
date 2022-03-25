import nextcord
from nextcord.ext import commands

from data.jabs import PHOTOJABS_URL

class Message(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self):
        channel = nextcord.utils.get(self.client.get_all_channels(), name='фотоjabs')
        # for message in channel.history():
        #     for attachment in message.attachments:
        #         PHOTOJABS_URL.append(attachment.url)

def setup(client):
    client.add_cog(Message(client))