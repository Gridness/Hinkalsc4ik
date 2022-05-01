import nextcord

def build_embed(client, title, description, color, has_author = True, has_footer = False, footer_text = None, hasImage = False, imageUrl = None):
    """Builds and returns an embed message with flexible settings of your choice"""
    embed = nextcord.Embed(title=title, description=description, color=color)
    if has_author:
        embed.set_author(client.user)
    if has_footer:
        embed.set_footer(text=footer_text)
    if hasImage:
        embed.set_image(url=imageUrl)
    return embed