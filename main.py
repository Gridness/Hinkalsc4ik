"""
Pelmenolog v2.0 (c) Gridness, Wasyas
This software is licensed under the GNU GPL 3.0 license. All rights reserved
The project is open-source. You can use its code wherever and however you want
"""
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
    
    load_dotenv()
    client = commands.Bot(command_prefix = os.getenv("PREFIX"), intents = intents)

    log('Loading extensions...', WARNING_LEVEL['medium'])

    loadExtensions(client, 'cogs', './cogs')
    loadExtensions(client, 'commands', './commands')

    log('Extensions loaded', WARNING_LEVEL['medium'])

    client.run(os.getenv("TOKEN"))

if __name__ == '__main__':
    main()