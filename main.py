"""To do."""

from objects import Commander, Card
from simulation import simulate

commander = Commander('wuub')

cards = ((
    Card(land=True, mana='wu'),
    Card(land=False, mana=''),
    Card(land=True, mana='u'),
    Card(land=True, mana='w'),
    Card(land=False, mana=''),
    Card(land=False, mana=''),
    Card(land=False, mana=''),
    Card(land=False, mana=''),
    Card(land=False, mana=''),
    Card(land=True, mana='wubrg'),
    Card(land=True, mana='wubrg'),
    Card(land=True, mana='b'),
))

print("You need to draw",
      round(simulate(commander, cards), 1),
      "cards to have access to all the mana needed to cast your commander.")

