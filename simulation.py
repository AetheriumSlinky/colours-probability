"""Execute the game simulation."""

from objects import Card, Commander, Deck, Game

cards_list = [Card(land=True, mana='wu'),
              Card(land=False, mana=''),
              Card(land=True, mana='u'),
              Card(land=True, mana='w'),
              Card(land=False, mana=''),
              Card(land=False, mana=''),
              Card(land=False, mana=''),
              Card(land=False, mana=''),
              Card(land=False, mana=''),
              Card(land=True, mana='wubrg'),
              Card(land=True, mana='wubrg'),
              Card(land=True, mana='b')]

card_counts = []
for _ in range(10000):

    new_game = Game(Commander('wubc'), Deck(tuple(cards_list)))
    new_game.play_game()
    card_counts.append(new_game.draw_count)

print("You need to draw",
      round(sum(card_counts) / 10000, 1),
      "cards to have access to all the mana needed to cast your commander.")
