"""To do."""
import sys

from func.exceptions import ExitProgram, SkipToBeginning
from func.query import Query


def main():
    query = Query()
    query.hello()
    try:
        query.ask_commander()
        query.ask_decklist()
        query.create_deck()
        query.print_result()
    except SkipToBeginning as e:
        print(e)
    except ExitProgram as e:
        print(e)
        sys.exit()


if __name__ == '__main__':
    while True:
        main()
        input("This simulation is complete. Press 'Enter' to try again!")