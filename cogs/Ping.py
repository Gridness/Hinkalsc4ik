from nextcord.ext import commands, tasks

from utils.log import log
from data.settings import PING_LOOP_TIME
from data.warningLevel import WARNING_LEVEL

class Ping(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @tasks.loop(seconds=PING_LOOP_TIME)
    async def getPing(self):
        latency = round(self.client.latency * 1000, 2)

        log(f'Ping: {latency} ms')
        if latency >= 300:
            log('High latency. The bot may be slow to respond', WARNING_LEVEL['medium'])
        elif latency >= 500:
            log('Extreme latency. The bot may not work properly. Try to /reload the bot or check discord servers\' status', WARNING_LEVEL['high'])

def setup(client):
    client.add_cog(Ping(client))