import func.exceptions as ex
from func.exceptions import CommanderNotFoundInDB
from func.simulation import simulate
from func.parse_sqlite import FromDatabase


class UserInputs:
    def __init__(self):
        self.commander_name = ''
        self.deck_list = {}


class Query:
    def __init__(self):
        self.from_database = FromDatabase('cards.db')
        self.user_input = UserInputs()
        self.commander = None
        self.cards = None

    @staticmethod
    def hello():
        print("""
Hello!
Make sure your deck contains exactly 99 cards in the main board, no side board and only one commander.
(Partner commanders are not implemented, yet.)
In the Moxfield deck view click:
    -> ⋮More
    -> Export
    -> Copy for MTGO""")

    def ask_commander(self):
        while not self.commander:
            self.user_input.commander_name = input("Enter your commander's exact name here and press 'Enter'.\n")
            try:
                self.commander = self.from_database.find_commander(self.user_input.commander_name)
            except CommanderNotFoundInDB as e:
                print(e)

    def ask_decklist(self):
        print("Paste the 'Copy for MTGO' decklist AS-IS, with the card counts in the front.")
        card_input = True
        while card_input:
            card_input = input()
            if card_input:
                count = int(card_input[0:2])
                name = card_input[card_input.index(' ') + 1:]
                self.user_input.deck_list[name] = count
        print()
        print("I registered", len(self.user_input.deck_list), "differently named cards, excluding the commander.")

    def create_deck(self):
        name: str
        deck_list = []
        for name in self.user_input.deck_list.keys():
            for count in range(self.user_input.deck_list[name]):
                deck_list.append(name)
        self.cards = tuple(self.from_database.find_cards(deck_list))
        print("I created a library with", len(deck_list), "cards in it, excluding the commander.")

    def print_result(self):
        print("You need to draw",
              round(simulate(self.commander, self.cards), 1),
              "cards to have access to all the colours - from your lands - needed to cast your commander.")
