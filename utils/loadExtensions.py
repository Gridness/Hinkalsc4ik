import os
from nextcord.ext import commands

from utils.log import log
from data.warningLevel import WARNING_LEVEL
from utils.rollout import rollout

def loadExtensions(client: commands.Bot, extensionType: str, relativeExtensionsPath: str, loadType: str = 'load') -> None:
    """Loads or reloads all extensions of the bot"""
    if loadType == 'load':
        try:
            for filename in os.listdir(relativeExtensionsPath):
                if filename.endswith(".py"):
                    client.load_extension(f'{extensionType}.{filename[:-3]}')
                    if extensionType == 'command':
                        rollout(client)
                    log(f'{filename[:-3]} loaded', WARNING_LEVEL['medium'])
        except Exception:
            log('An error occured while loading extensions', WARNING_LEVEL['high'])
            raise Exception('Failed to load extensions')
    elif loadType == 'reload':
        try:
            for filename in os.listdir(relativeExtensionsPath):
                if filename.endswith(".py"):
                    client.reload_extension(f'{extensionType}.{filename[:-3]}')
                    if extensionType == 'command':
                        rollout(client)
                    log(f'{filename[:-3]} loaded', WARNING_LEVEL['medium'])
        except Exception:
            log('An error occured while loading extensions', WARNING_LEVEL['high'])
            raise Exception('Failed to load extensions')
    else:
        log('Unknown extensions loading type', WARNING_LEVEL['medium'])