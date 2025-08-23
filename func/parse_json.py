"""Parses the raw JSON card data into a new databse object with less information."""


class IllegalCard(Exception):
    pass


class JSONCard:
    def __init__(self, card_data):
        self.card_data = card_data[0]
        self.name = ''
        self.oracle = ''
        self.land = False
        self.commander = False
        self.produces = ''
        self.cost = ''
        self.mv = 0

    def parse_card(self):
        try:
            if (('Land' in self.card_data['types'])
                    and (self.card_data['legalities']['commander'] == 'Legal')
                    and ('//' not in self.card_data['name'])):
                self.__land()
            elif self.card_data['leadershipSkills']['commander'] and self.card_data['legalities']['commander']:
                self.__commander()
        except KeyError:
            self.__nonland()
        self.card_data = None

    def __land(self):
        self.name = self.card_data['name']
        self.land = True
        self.oracle = self.card_data['text']
        self.__mana_production()

    def __commander(self):
        self.name = self.card_data['name']
        self.commander = True
        self.__mana_cost()
        self.__mana_value()

    def __nonland(self):
        pass

    def __mana_production(self):
        # Separate Basics first
        if 'Basic' in self.card_data['supertypes']:
            identity = ''.join([char.lower() for char in self.card_data['colorIdentity']])
            if not identity:  # Wastes
                self.produces = 'c'
            else:
                self.produces = identity

        # Separate all-producing lands without an identity
        elif ': Add one mana of any' in self.oracle:
            self.produces = 'wubrg'

        # Separate Fetch-lands and let them produce any colour
        elif 'Sacrifice this land: Search your library' in self.oracle:
            self.produces = 'wubrg'

        # Separate miscellaneous lands with no colour production but an identity regardless
        elif (': Add {C}.' in self.oracle
              and '} or {' not in self.oracle
              and len(self.card_data['colorIdentity']) > 0):
            self.produces = 'c'

        # Separate Filter-lands with their hybrid mana, buuuutt treat them as dual lands
        elif '/' in self.oracle and (('/+' or '/-') not in self.oracle):
            self.produces = ''.join([char.lower() for char in self.card_data['colorIdentity']])

        # Clump the rest together, whatever yo
        else:
            self.produces = 'c'

    def __mana_cost(self):
        cost: str = self.card_data['manaCost']
        cost = ''.join([char.casefold() for char in cost[1:-1].split(sep='}{')])
        self.cost = cost

    def __mana_value(self):
        self.mv = self.card_data['manaValue']
