from func.simulation import simulate
from func.parse_sqlite import FromDatabase


class UserInputs:
    def __init__(self):
        self.commander_name = ''
        self.deck_list = []


class Query:
    def __init__(self):
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
        self.user_input.commander_name = input("Enter your commander's exact name here and press 'Enter'.\n")

    def ask_decklist(self):
        cardname = input("Paste the 'Copy for MTGO' decklist here.\n")
        self.user_input.deck_list.append(cardname[2:])
        while cardname:
            cardname = input()
            if cardname:
                for count in range(int(cardname[0])):
                    self.user_input.deck_list.append(cardname[2:])
        print()
        print("I registered", len(self.user_input.deck_list), "different cards, excluding the commander.")

    def create_deck(self):
        from_database = FromDatabase('cards.db',
                                     self.user_input.commander_name,
                                     self.user_input.deck_list)

        self.commander = from_database.find_commander()
        self.cards = tuple(from_database.find_cards())

    def print_result(self):
        print("You need to draw",
              round(simulate(self.commander, self.cards), 1),
              "cards to have access to all the colours - from your lands - needed to cast your commander.")
