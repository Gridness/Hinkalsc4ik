import os
from utils.loadExtensions import loadExtensions

try:
    import nextcord
    from nextcord.ext import commands
    from dotenv import load_dotenv
except ImportError:
    os.system('pip install -U nextcord python-dotenv')
    import nextcord
    from nextcord.ext import commands
    from dotenv import load_dotenv

from utils.log import log
from data.warningLevel import WARNING_LEVEL

def main():

    intents = nextcord.Intents.all()
    intents.members = True
    
    client = commands.Bot(command_prefix = 'abobus!', intents = intents)

    log('Loading extensions...', WARNING_LEVEL['medium'])

    loadExtensions(client, 'cogs', './cogs')
    loadExtensions(client, 'commands', './commands')
    
    # try:
    #     for filename in os.listdir('./cogs'):
    #         if filename.endswith(".py"):
    #             client.load_extension(f'cogs.{filename[:-3]}')
    #             log(f'{filename[:-3]} loaded', WARNING_LEVEL['medium'])
    # except Exception:
    #     log('An error occured while loading extensions', WARNING_LEVEL['high'])
    #     raise Exception('Failed to load extensions')

    # try:
    #     for filename in os.listdir('./commands'):
    #         if filename.endswith(".py"):
    #             client.load_extension(f'commands.{filename[:-3]}')
    #             log(f'{filename[:-3]} loaded', WARNING_LEVEL['medium'])
    # except Exception:
    #     log('An error occured while loading extensions', WARNING_LEVEL['high'])
    #     raise Exception('Failed to load extensions')

    log('Extensions loaded', WARNING_LEVEL['medium'])

    load_dotenv()
    client.run(os.getenv("TOKEN"))

if __name__ == '__main__':
    main()