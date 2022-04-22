import aiosqlite
import nextcord
import random
from nextcord.ext import commands

from data.settings import DEFAULT_DB_PATH, EMBED_COLOR, SERVER_ID
from data.warningLevel import WARNING_LEVEL
from utils.buildEmbed import build_embed
from utils.log import log
from utils.parser.parser import parse

class Joke(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    server_id = SERVER_ID

    @nextcord.slash_command(name='joke', description='Returns a random joke', guild_ids=[server_id])
    async def joke(self, 
    interaction: nextcord.Interaction, 
    source: str = nextcord.SlashOption(description='Choose the source of the joke', choices={'1': 'db', '2': 'anekdot.ru'})):
        if source == 'db':
            try:
                async with aiosqlite.connect(DEFAULT_DB_PATH) as db:
                    async with db.cursor() as cursor:
                        await cursor.execute('SELECT joke FROM jokes ORDER BY RANDOM() LIMIT 1')
                        joke = await cursor.fetchone()
            except Exception:
                log('Unable to execute query. Either the database is unavailable or the query itself is not proper', WARNING_LEVEL['high'])
                
            await interaction.channel.send(embed=build_embed(self.client, 'ВНИМАНИЕ: АНЕКДОТ', joke, EMBED_COLOR, False))
        elif source == 'anekdot.ru':
            await interaction.channel.send(embed=build_embed(self.client, 'ВНИМАНИЕ: АНЕКДОТ', parse()[random.randint(0, len(parse()))], EMBED_COLOR, False))


def setup(client):
    client.add_cog(Joke(client))