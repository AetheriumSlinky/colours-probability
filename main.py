"""To do."""

from func.query import Query


def main():
    query = Query()
    query.hello()
    query.ask_commander()
    query.ask_decklist()
    query.create_deck()
    query.print_result()
    input("This simulation is complete. Press 'Enter' to exit!")


if __name__ == '__main__':
    main()
