from nextcord.ext import commands

from data.settings import SERVER_ID

async def rollout(client: commands.Bot) -> None:
    guild = client.get_guild(SERVER_ID)
    await guild.rollout_application_commands()