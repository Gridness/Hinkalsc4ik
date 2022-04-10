import aiosqlite
import nextcord
from nextcord.ext import commands

from data.settings import DEFAULT_DB_PATH, EMBED_COLOR, SERVER_ID
from utils.buildEmbed import build_embed

class Joke(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    server_id = SERVER_ID

    @nextcord.slash_command(name='joke', description='Returns a random joke', guild_ids=[server_id,])
    async def joke(self, interaction: nextcord.Interaction):      
        async with aiosqlite.connect(DEFAULT_DB_PATH) as db:
            async with db.cursor() as cursor:
                await cursor.execute('SELECT joke FROM jokes ORDER BY RANDOM() LIMIT 1')
                joke = await cursor.fetchone()
                
        await interaction.channel.send(embed=build_embed(self.client, 'ВНИМАНИЕ: АНЕКДОТ', joke, EMBED_COLOR, False))
            

def setup(client):
    client.add_cog(Joke(client))