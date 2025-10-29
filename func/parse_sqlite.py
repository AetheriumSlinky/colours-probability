"""Hrmph."""
import sqlite3

from func.exceptions import TooManyCommanders, CommanderNotFoundInDB
from func.objects import Card, Commander

class FromDatabase:
    def __init__(self, database_path: str):
        self.database = database_path

    def find_commander(self, commander_name: str) -> Commander:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM commanders WHERE name = ?", (commander_name,))
        commander_match = cursor.fetchall()
        cursor.close()
        conn.close()

        if len(commander_match) > 1:
            raise TooManyCommanders("Too many Commander card matches in the card database. Check spelling.")

        elif not commander_match:
            raise CommanderNotFoundInDB("Commander name not found in the card database. Trying Scryfall.")

        return Commander(name=commander_match[0][0],
                         mv=commander_match[0][1],
                         cost=commander_match[0][2])

    def find_cards(self, card_names: list[str]) -> list[Card]:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cards = []
        for name in card_names:
            cursor.execute("SELECT * FROM lands WHERE name = ?", (name,))
            result = cursor.fetchone()
            if not result:
                cards.append(Card(False, ''))
            else:
                cards.append(Card(True, result[1]))

        cursor.close()
        conn.close()
        return cards
