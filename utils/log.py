from rich.console import Console

from data.warningLevel import WARNING_LEVEL

def log(logText, color = WARNING_LEVEL['default'], logType = 'log'):
    console = Console()

    if logType == 'log':
        console.log(f'[{color}]{logText}[/{color}]')
    elif logType == 'print':
        console.print(f'[{color}]{logText}[/{color}]')
    else:
        console.log(f'[{color}]Unknown print type \"{logType}\"[/{color}]')