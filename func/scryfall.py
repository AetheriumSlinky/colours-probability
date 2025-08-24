import requests

from func.exceptions import CommanderNotFoundFromSF
from func.objects import Commander

class ScryfallCard:
    def __init__(self, name):
        self.name = name
        self.headers = {'User-Agent': 'AetheriumSlinky/ColoursProbability/0.1.0', 'Accept': '*/*'}
        self.card_json = None

    def request_card_data(self) -> Commander:
        potential_card_json = requests.get(
            url=f'https://api.scryfall.com/cards/search?q={self.name}+is%3Acommander+legal%3Acommander',
            headers=self.headers,
        )
        response = potential_card_json.json()
        if response['object'] == 'error':
            raise CommanderNotFoundFromSF("No Commander cards found with this name. Check spelling and legality.")
        if response['total_cards'] == 1:
            self.card_json = response['data'][0]
        mana_cost = self.card_json['mana_cost'][1:-1].split('}{')
        commander = Commander(name=self.card_json['name'],
                              mv=self.card_json['cmc'],
                              cost=''.join([char.casefold() for char in mana_cost]))
        return commander
