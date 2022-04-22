import os

try:
    from rich.console import Console
except ImportError:
    os.system('pip install -U rich')
    from rich.console import Console

from data.warningLevel import WARNING_LEVEL

def log(logText: str, color: str = WARNING_LEVEL['default'], logType: str = 'log') -> None:
    console = Console()

    if logType == 'log':
        console.log(f'[{color}]{logText}[/{color}]')
    elif logType == 'print':
        console.print(f'[{color}]{logText}[/{color}]')
    else:
        console.log(f'[{color}]Unknown print type \"{logType}\"[/{color}]')