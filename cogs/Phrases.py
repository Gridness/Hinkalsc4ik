import nextcord
from nextcord.ext import commands, tasks

from data.settings import STATUS_LOOP_TIME
from utils.phrases.presencePhrases import PRESENCE_PHRASES
from utils.log import log
from utils.randomHandler import pickAndRemoveRepeatingStatuses

class Phrases(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @tasks.loop(seconds=STATUS_LOOP_TIME)
    async def changePresence(self):
        newPresence = pickAndRemoveRepeatingStatuses(PRESENCE_PHRASES)
        await self.client.change_presence(activity=nextcord.Game(name=newPresence))

        log(f'Changed presence to {newPresence}')

def setup(client):
    client.add_cog(Phrases(client))