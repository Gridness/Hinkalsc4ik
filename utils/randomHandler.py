import random

from utils.phrases.presencePhrases import PRESENCE_PHRASES

previousStatuses = []

def pickAndRemoveRepeatingStatuses(statuses):
    global previousStatuses
    
    # async with aiosqlite.connect(DEFAULT_DB_PATH) as db:
    #     async with db.cursor() as cursor:
    #         await cursor.execute('SELECT status FROM statuses ORDER BY RANDOM() LIMIT 1')
    #         status = await cursor.fetchone()
    status = random.choice(statuses)
    while status in previousStatuses:
        status = random.choice(statuses)

    previousStatuses.append(status)
    if len(previousStatuses) == len(PRESENCE_PHRASES):
        previousStatuses.clear()

    return status