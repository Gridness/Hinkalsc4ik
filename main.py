import os
import sys

try:
    import nextcord
    from nextcord.ext import commands
    from dotenv import load_dotenv
except ImportError:
    os.system('pip install -U nextcord python-dotenv')
    import nextcord
    from nextcord.ext import commands
    from dotenv import load_dotenv

# from cogs.Join import Join
# from cogs.Phrases import Phrases
# from cogs.Ready import Ready
# from cogs.Ping import Ping

from utils.log import log
from data.warningLevel import WARNING_LEVEL

def main():

    intents = nextcord.Intents.all()
    intents.members = True
    
    client = commands.Bot(command_prefix = 'abobus!', intents = intents)
    
    # cogs = [Ready, Ping, Join, Phrases]
    # for i in range(len(cogs)):
    #     cogs[i].setup(client)

    log('Loading extensions...', WARNING_LEVEL['medium'])
    try:
        for filename in os.listdir('./cogs'):
            if filename.endswith(".py"):
                client.load_extension(f'cogs.{filename[:-3]}')
                log(f'{filename[:-3]} loaded', WARNING_LEVEL['medium'])
    except Exception:
        log('An unknown error occured while loading extensions', WARNING_LEVEL['high'])
        raise Exception('Failed to load extensions')

    try:
        for filename in os.listdir('./commands'):
            if filename.endswith(".py"):
                client.load_extension(f'cogs.{filename[:-3]}')
                log(f'{filename[:-3]} loaded', WARNING_LEVEL['medium'])
    except Exception:
        log('An unknown error occured while loading extensions', WARNING_LEVEL['high'])
        raise Exception('Failed to load extensions')

    log('Extensions loaded', WARNING_LEVEL['medium'])
    
    extDataDir = os.getcwd()
    if getattr(sys, 'frozen', False):
        extDataDir = sys._MEIPASS
    load_dotenv(dotenv_path=os.path.join(extDataDir, '.env'))
    client.run(os.getenv("TOKEN"))

if __name__ == '__main__':
    main()