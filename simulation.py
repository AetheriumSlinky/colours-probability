"""Execute the game simulation."""

from objects import Commander, Deck, Game
from constants import Simulation

def simulate(commander: Commander, cards: tuple) -> float:
    draw_counts = []
    for _ in range(Simulation.CYCLES):
        deck = Deck(cards)
        new_game = Game(commander, deck)
        new_game.play_game()
        draw_counts.append(new_game.draw_count)
    return sum(draw_counts) / Simulation.CYCLES
