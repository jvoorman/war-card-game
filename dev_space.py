# reuasable script to test small chunks of code

import requests

class Deck(object):
    """This is the deck that we're gonna use for our card game"""
    # TBH you could probably replace this with simply a deck_id
    def __init__(self):
        deck = self.get_shuffled_deck()
        self.deck = deck
        self.deck_id = deck['deck_id']
        self.shuffled = deck['shuffled']
        self.remaining = deck['remaining']

    def get_shuffled_deck(self):
        r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/')
        return r.json()

    def draw_from_deck(self, num_cards):
        # returns card codes formatted to add to pile
        r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={num_cards}').format(
                deck_id = deck.deck_id,
                num_cards = str(num_cards)
                )
            )
        cards = r.json()['cards']
        card_codes_list = []
        for i in range(len(cards)):
            card_codes_list.append(cards[i]['code'])
        card_codes_str = ",".join(card_codes_list)
        return card_codes_str


deck = Deck()
deck_id = deck.deck_id
print(deck.draw_from_deck(3))

class CardPile(object):
    """A pile of cards that we can use for various things"""
    def __init__(self, deck_id, pile_name, cards_to_add):
        pile = self.create_new_pile(deck_id, pile_name, cards_to_add)
        self.deck_id = deck_id
        self.name = pile_name
        self.remaining = pile['remaining']

    def create_new_pile(self, deck_id, pile_name, cards_to_add):
        r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={cards_to_add}').format(
                deck_id = deck_id,
                pile = ('{player}_pile').format(player = pile_name),
                cards_to_add = cards_to_add
                )
            )
        return r.json()
    
    def get_card_codes_list(self):
        r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/list/').format(
                deck_id = self.deck_id,
                pile = ('{player}_pile').format(player = self.name)
                )
            )
        cards = r.json()['cards']
        card_codes_list = []
        for i in range(len(cards)):
            card_codes_list.append(cards[i]['code'])
        return card_codes_list

         
jenna_pile = CardPile(deck_id, 'jenna', deck.draw_from_deck(1))

