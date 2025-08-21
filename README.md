Simulates playing a game of the EDH / Commander format in Magic: The Gathering.

The simulation produces an approximation of how many cards one needs to draw
in order to have all the land cards producing mana (including colours) required to cast the commander.

Roughly 10 000 iterations (defined in the constants.py file) will produce a result that is accurate to one decimal (roughly).
This is accounted for in the print text's rounding.

How to run:
- Run the main.py file.
- Note that currently you need to individually define each card's properties in the main.py file.

Inputs:
- A list of cards (99) in the deck.
- Commander card (1).

Output:
- The number of cards needed to draw in order to cover the casting cost of the Commander.

TO DO:
- Creating an user interface of some sorts.
- Input method: copy-pasting card names or a Moxfield link.
- Card properties parsing based on the card's name only.
- Account for edge cases such as two commanders, Fetch Lands, hybrid mana costs, etc...
