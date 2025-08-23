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
    def handle_input_exceptions(func):
        """
        Handles 'exit' and 'clear' ('skip') inputs. Throws errors if inputs are not suitable, i.e. not a single string.
        :param func: A function that strictly takes a string argument with the input() function.
        :return: Function unless input was 'exit', 'clear' or 'skip'.
        """

        def wrapper(*args, **kwargs):
            """Wrapper."""
            new_arg = ([arg for arg in args if arg is not None]
                       + [kwarg for kwarg in kwargs.values() if kwarg is not None])

            if len(new_arg) != 1:
                raise ValueError(
                    f" > Unexpected number of args or kwargs (was {len(new_arg)}, should be 1). "
                    f"The handle_input_exceptions decorator is probably used incorrectly. "
                    f"The input should be a single str. Exiting program."
                )

            if not isinstance(new_arg[0], str):
                raise TypeError(
                    f" > Invalid data type (was {type(new_arg[0]).__name__}, should be str). "
                    f"The handle_input_exceptions decorator is probably used incorrectly. "
                    f"The input should be a single str. Exiting program."
                )
            new_arg = ''.join(new_arg).lower()

            while True:

                if new_arg in ['clear', 'skip']:
                    raise ex.SkipToBeginning("Clear command was given.")
                elif new_arg == 'exit':
                    raise ex.ExitProgram("Exit command was given.")
                elif not new_arg:
                    print("Empty input. Please try again or enter 'skip' or 'exit'.")
                else:
                    try:
                        return func(new_arg)
                    except ex.InvalidInput as e:
                        print(e)

                new_arg = input("Try again to do whatever you were supposed to do:\n").lower()

        return wrapper

    @staticmethod
    @handle_input_exceptions
    def query_input(prompt: str) -> str:
        return input(prompt)

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
