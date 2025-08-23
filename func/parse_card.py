"""Parses the raw JSON card data into a new databse object with less information."""

class IllegalCard(Exception):
    pass


class JSONCard:
    def __init__(self, card_data):
        self.card_data = card_data[0]
        self.name = ''
        self.land = False
        self.commander = False
        self.produce = ''
        self.cost = ''
        self.mv = 0

    def parse_card(self):
        try:
            if (('Land' in self.card_data['types'])
                    and (self.card_data['legalities']['commander'] == 'Legal')
                    and ('//' not in self.card_data['name'])):
                self.__land()
            elif self.card_data['leadershipSkills']['commander']:
                self.__commander()
        except KeyError:
            self.__nonland()
        self.card_data = None

    def __land(self):
        self.name = self.card_data['name']
        self.land = True
        self.__mana_produce()

    def __commander(self):
        self.name = self.card_data['name']
        self.commander = True
        self.__mana_cost()
        self.__mana_value()

    def __nonland(self):
        pass

    def __mana_produce(self):
        self.produce = ''.join([char.lower() for char in self.card_data['colorIdentity']])
        if not self.produce:
            self.produce = 'c'

    def __mana_cost(self):
        cost: str = self.card_data['manaCost']
        cost = ''.join([char.casefold() for char in cost[1:-1].split(sep='}{')])
        self.cost = cost

    def __mana_value(self):
        self.mv = self.card_data['manaValue']
