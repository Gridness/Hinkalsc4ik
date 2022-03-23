import random

from utils.phrases.presencePhrases import PRESENCE_PHRASES

previousStatuses = []

def pickAndRemoveRepeatingStatuses(statuses):
    global previousStatuses
    
    status = random.choice(statuses)
    while status in previousStatuses:
        status = random.choice(statuses)

    previousStatuses.append(status)
    if sorted(previousStatuses) == sorted(PRESENCE_PHRASES):
        previousStatuses.clear()