import os

from extract import CMDR_CURATED_FILES, CMDR_DECKNAMES

for deckname in CMDR_DECKNAMES:
    for decklist in CMDR_CURATED_FILES:
        if deckname in decklist:
