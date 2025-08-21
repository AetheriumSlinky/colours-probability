"""Holds the different object types needed for the simulation."""

import random
import itertools

from constants import Sorting

class Card:
    def __init__(self, land: bool, mana: str):
        self.land = land
        self.mana = mana


class Commander:
    def __init__(self, cost: str):
        self.mv = len(cost)
        self.colours = set([char for char in cost if char in 'wubrg'])
        self.generic = cost.count('c')


class ManaPool:
    def __init__(self):
        self.mana = []

    def add_land(self, card: Card):
        self.mana.append(card.mana)

    def produces(self) -> set:
        return set(itertools.product(*[m for m in self.mana if m in 'wubrg']))


class Deck:
    def __init__(self, cards: tuple[Card, ...]):
        self.cards = cards
        self.remaining_cards = list(cards)

    def new_card(self) -> Card:
        card = random.choice(self.remaining_cards)
        self.remaining_cards.remove(card)
        return card


class Game:
    def __init__(self, commander: Commander, deck: Deck):
        self.draw_count = 0
        self.commander = commander
        self.deck = deck
        self.mana_pool = ManaPool()

    def start(self):
        self.draw_count = 0
        for _ in range(7):
            new_card = self.deck.new_card()
            if new_card.land:
                self.mana_pool.add_land(new_card)

    def new_turn(self):
        self.draw_count += 1
        new_card = self.deck.new_card()
        if new_card.land:
            self.mana_pool.add_land(new_card)

    def success(self) -> bool:
        if len(self.mana_pool.mana) >= self.commander.mv:
            for colours in self.mana_pool.produces():
                if self.commander.colours.issubset(colours):
                    return True
        return False

    def play_game(self):
        success = False
        while not success:
            self.new_turn()
            success = self.success()
