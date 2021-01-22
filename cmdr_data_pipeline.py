print("Starting... CMDR DATA PIPELINE")
from replace import *
from logging import *
from extract import *

# __main__
for deck in CMDR_RAW_FILES:
    deck_object = Extract(deck).createDeck()
