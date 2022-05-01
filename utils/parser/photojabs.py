import nextcord

from data.settings import JABS_PARSING_LIMIT

async def get_jabs(channel: nextcord.TextChannel) -> None:
    async for message in channel.history(limit = JABS_PARSING_LIMIT):
        for attachment in message.attachments:
            attachment.save()