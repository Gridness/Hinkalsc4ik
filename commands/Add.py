import aiosqlite
import nextcord
from nextcord.ext import commands

from data.settings import DEFAULT_DB_PATH, EMBED_COLOR, SERVER_ID
from utils.buildEmbed import build_embed

server_id = SERVER_ID

class Add(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @nextcord.slash_command(name='add', description='Adds something to the database', guild_ids=[server_id])
    async def add(self, 
    interaction: nextcord.Interaction, 
    type: str = nextcord.SlashOption(description='A joke or a status?', choices={'joke': 'joke', 'status': 'status'}), 
    data: str = nextcord.SlashOption(description='What exactly do you want to add?')):
        if type == 'joke':
            async with aiosqlite.connect(DEFAULT_DB_PATH) as db:
                async with db.cursor() as cursor:
                    await cursor.execute('INSERT INTO jokes (joke) VALUES (?)', (data))
                await db.commit()

            await interaction.channel.send(embed=build_embed(self.client, 'Ваш крутой анек был добавлен', 'Шо?', EMBED_COLOR, False))
        elif type == 'status':
            async with aiosqlite.connect(DEFAULT_DB_PATH) as db:
                async with db.cursor() as cursor:
                    await cursor.execute('INSERT INTO statuses (status) VALUES (?)', (data))
                await db.commit()

            await interaction.channel.send(embed=build_embed(self.client, 'Ваш крутой статус был добавлен', 'Шо?', EMBED_COLOR, False))
        else:
            await interaction.channel.send(embed=build_embed(self.client, '?', '', EMBED_COLOR, False))

def setup(client):
    client.add_cog(Add(client))
