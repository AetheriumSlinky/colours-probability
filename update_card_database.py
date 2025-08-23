"""To update you need to download the AutomicCards.json file from MTGJSON."""

import json
import sqlite3

from func.parse_json import JSONCard

if __name__ == '__main__':
    with open('AtomicCards.json', encoding='utf-8') as c:
        all_card_data = json.load(c)

    lands = []
    commanders = []
    for card_data in all_card_data['data'].values():
        new_card = JSONCard(card_data)
        new_card.parse_card()
        if new_card.land:
            lands.append(new_card)
        elif new_card.commander:
            commanders.append(new_card)

    conn = sqlite3.connect('cards.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS lands")
    cursor.execute("DROP TABLE IF EXISTS commanders")

    create_lands_table = """
        CREATE TABLE lands (
            name VARCHAR(100),
            mana VARCHAR(6)
        );
    """
    cursor.execute(create_lands_table)

    create_commanders_table = """
        CREATE TABLE commanders (
            name VARCHAR(100),
            mv INT,
            cost VARCHAR(15)
        );
    """
    cursor.execute(create_commanders_table)

    for card in lands:
        cursor.execute("INSERT INTO lands (name, mana) VALUES (?, ?);",
                       (card.name, card.produces))

    for card in commanders:
        cursor.execute("INSERT INTO commanders (name, mv, cost) VALUES (?, ?, ?);",
                       (card.name, card.mv, card.cost))

    conn.commit()
    cursor.close()
    conn.close()

    input("Database updated. Press 'Enter' to exit.")
