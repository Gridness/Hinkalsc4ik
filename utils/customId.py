from data.meta import META

def customId(view: str, id: int) -> str:
    return f'{META["name"]}:{view}:{id}'