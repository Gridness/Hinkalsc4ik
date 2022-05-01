import nextcord
from nextcord.ext import commands

from data.settings import EMBED_COLOR, SERVER_ID
from data.warningLevel import WARNING_LEVEL
from utils.buildEmbed import build_embed
from utils.log import log

server_id = SERVER_ID

class Purge(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @nextcord.slash_command(name='purge', description='Removes all roles from a user', guild_ids=[server_id])
    async def purge(self, 
    interaction: nextcord.Interaction, 
    member: nextcord.Member = nextcord.SlashOption(description='Declare a member to be purged'), 
    jail: str = nextcord.SlashOption(
        description='Temporary does nothing', 
        choices={'jail': 'jail', 'no-jail': 'no-jail'})):
        if jail is None or jail == '' or jail == 'no-jail':
            for role in member.roles:
                try:
                    await member.remove_roles(role)
                except:
                    log(f'Unable to remove role {role}', WARNING_LEVEL['medium'])
            await member.send(embed=build_embed(self.client, 'НАКОЛОЧКИ, НАКОЛОЧКИ', 'ГОП, ТАТУИРОВОЧКИ', EMBED_COLOR, False))
            log(f'{member} has lost all his roles thanks to {interaction.user.id}. Oh no')
        else:
            pass

def setup(client):
    client.add_cog(Purge(client))