Simulates playing a game of the EDH / Commander format in Magic: The Gathering.

The simulation produces an approximation of how many cards one needs to draw
in order to have all the land cards producing mana (including colours) required to cast the commander.

Roughly 10 000 iterations (defined in the constants.py file) will produce a result
that is accurate to one decimal (roughly). This is accounted for in the print text's rounding.

How to run:
- Run the main.py file. For the time being only a few test cards are provided.
- The provided cards.db should contain all Commander-legal Lands and commanders. (Updated: 22/8/2025.)
- In case the database needs updating download https://mtgjson.com/downloads/all-files/#atomiccards.
- Place the downloaded JSON in the root directory and run update_card_database.py.

Inputs:
- A list of cards (99) in the deck.
- Commander card (1).

Output:
- The number of cards needed to draw in order to cover the casting cost of the Commander.

TO DO:
- Create a user interface of some sorts.
- Input method: copy-paste card names or a Moxfield link.
- Account for edge cases such as two commanders, Fetch Lands, hybrid mana costs, etc...
