"""Hrmph."""
import sqlite3

from func.exceptions import FetchException
from func.objects import Card, Commander

class FromDatabase:
    def __init__(self, database_path: str, commander_name: str, cardnames: list[str]):
        self.database = database_path
        self.commander_name = commander_name
        self.cardnames = cardnames

    def find_commander(self) -> Commander:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM commanders WHERE name = ?", (self.commander_name,))
        commander_match = cursor.fetchall()

        if len(commander_match) > 1:
            cursor.close()
            conn.close()
            raise FetchException("Too many Commander card matches in the card database.")

        cursor.close()
        conn.close()
        return Commander(commander_match[0][0], commander_match[0][1], commander_match[0][2])

    def find_cards(self) -> list[Card]:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cards = []
        for name in self.cardnames:
            cursor.execute("SELECT * FROM lands WHERE name = ?", (name,))
            result = cursor.fetchone()
            if not result:
                cards.append(Card(False, ''))
            else:
                cards.append(Card(True, result[1]))

        cursor.close()
        conn.close()
        return cards
