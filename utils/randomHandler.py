import random

from utils.phrases.presencePhrases import PRESENCE_PHRASES

previousStatuses = []

def pickAndRemoveRepeatingStatuses(statuses):
    global previousStatuses
    
    status = random.choice(statuses)
    while status in previousStatuses:
        status = random.choice(statuses)

    previousStatuses.append(status)
    if len(previousStatuses) == len(PRESENCE_PHRASES):
        previousStatuses.clear()

    return status