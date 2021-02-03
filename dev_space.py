# reuasable script to test small chunks of code

import requests
import game

deck = game.Deck()

jenna_pile = game.CardPile(deck.deck_id, 'jenna_draw', deck.draw_from_deck(4))


print(jenna_pile.get_card_codes_list())
print(jenna_pile.name)
print(jenna_pile.deck_id)
print(jenna_pile.remaining)