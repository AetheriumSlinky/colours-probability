"""To do."""
import sys
from func.query import Query


def main():
    query = Query()
    query.hello()
    query.ask_commander()
    query.ask_decklist()
    query.create_deck()
    query.print_result()


if __name__ == '__main__':
    while True:
        main()
        exit_condition = input("This simulation is complete. Press 'Enter' to try again or 'exit' to exit!")
        if exit_condition:
            sys.exit()