"""To do."""

from func.objects import Commander, Card
from func.simulation import simulate

def main():

    cards = ((
        Card(land=True, mana='wu'),
        Card(land=True, mana='r'),
        Card(land=True, mana='ur'),
        Card(land=True, mana='w'),
        Card(land=False, mana=''),
        Card(land=False, mana=''),
        Card(land=True, mana='b'),
        Card(land=True, mana='wurg'),
        Card(land=True, mana='wurg'),
        Card(land=True, mana='b'),
    ))

    commander = Commander('wr', 3)
    print("You need to draw",
          round(simulate(commander, cards), 1),
          "cards to have access to all the colours from your lands needed to cast your commander.")

    input()

    commander_2 = Commander('ww/r', 3)
    print("You need to draw",
          round(simulate(commander_2, cards), 1),
          "cards to have access to all the colours from your lands needed to cast your commander.")

if __name__ == '__main__':
    main()
