"""Holds the different object types needed for the simulation."""

import re
import random
import itertools

class Card:
    def __init__(self, land: bool, mana: str):
        self.land = land
        self.mana = mana


class Commander:
    def __init__(self, cost: str, mv: int):
        self.mv = mv
        self.colours = [tuple()]
        if '/' not in cost:
            self.colours = [tuple([char for char in cost if char in 'wubrg'])]  # [(wur)]
        else:
            self.__find_colours(cost)  # [(wur), (wuu)]
        numerals = ''.join([char for char in cost if char.isnumeric()])
        if numerals:
            self.generic = cost.count('c') + int(''.join([char for char in cost if char.isnumeric()]))
        else:
            self.generic = cost.count('c')

    def __find_colours(self, cost):
        colours: list[str] = []
        colour_pattern = re.compile(r"(?<!\/)([a-z])(?!\/)|(?:([a-z])\/([a-z]))")
        for match in colour_pattern.finditer(cost):
            colours.append(''.join(match.groups(default="")))
        self.colours = [c for c in itertools.product(*colours)]  # a list of tuples of characters


class ManaPool:
    def __init__(self):
        self.mana = []

    def add_land(self, card: Card):
        self.mana.append(card.mana)

    def produces(self) -> list:
        return list(itertools.product(*[m for m in self.mana if m in 'wubrg']))


class Deck:
    def __init__(self, cards: tuple[Card, ...]):
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

    def new_draw(self):
        self.draw_count += 1
        new_card = self.deck.new_card()
        if new_card.land:
            self.mana_pool.add_land(new_card)

    def success(self) -> bool:
        if self.draw_count >= self.commander.mv:
            pool_options = self.mana_pool.produces()
            commander_options = self.commander.colours
            for pool_tuple in pool_options:
                for commander_tuple in commander_options:
                    if all(option in pool_tuple for option in commander_tuple):
                        return True
        return False

    def play_game(self):
        success = False
        while not success:
            self.new_draw()
            success = self.success()
