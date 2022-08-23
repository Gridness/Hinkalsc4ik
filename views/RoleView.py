import nextcord
import random
from data.settings import EMBED_COLOR, MESSAGE_LIFECYCLE_DURATION, ROLE_ID

from utils.customId import customId
from utils.log import log
from utils.buildEmbed import build_embed
from utils.phrases.kickPhrases import KICK_PHRASES
from utils.phrases.rolePhrases import ROLE_PHRASES

class RoleView(nextcord.ui.View):
    def __init__(self, client):
        self.client = client
        super().__init__(timeout=None)

    async def handleClick(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        roleID = int(button.custom_id.split(':')[-1])
        role = interaction.guild.get_role(roleID)
        assert isinstance(role, nextcord.Role)

        await interaction.user.add_roles(role)
        log(f'{interaction.user} was given a role {role}')

        await interaction.user.send(embed=build_embed(self.client, random.choice(ROLE_PHRASES), '', EMBED_COLOR, False, hasImage=True, imageUrl=''))
        await interaction.delete_original_message(delay=MESSAGE_LIFECYCLE_DURATION)

    async def handleKickButtonClick(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        log(f'{interaction.user} was kicked')
        await interaction.user.send(embed=build_embed(self.client, random.choice(KICK_PHRASES), '', EMBED_COLOR, False))
        await interaction.user.kick(reason='Оскорбление бота по причине: не обязан')
        await interaction.delete_original_message(delay=MESSAGE_LIFECYCLE_DURATION)

    @nextcord.ui.button(label='Да я знаю', style=nextcord.ButtonStyle.primary, custom_id=customId("RoleView", ROLE_ID))
    async def getRole(self, button, interaction):
        await self.handleClick(button, interaction)

    @nextcord.ui.button(label='Нет, блин, твоя', style=nextcord.ButtonStyle.red, custom_id=customId("RoleViewKick", 1))
    async def getKicked(self, button, interaction):
        await self.handleKickButtonClick(button, interaction)
