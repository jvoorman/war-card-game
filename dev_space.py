# reuasable script to test small chunks of code

import requests
import game

class Deck(object):
    """This is the deck that we're gonna use for our card game"""
    # TBH you could probably replace this with simply a deck_id
    def __init__(self):
        deck = self.get_shuffled_deck()
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
                deck_id = self.deck_id,
                num_cards = str(num_cards)
                )
            )
        cards = r.json()['cards']
        card_codes_list = []
        for i in range(len(cards)):
            card_codes_list.append(cards[i]['code'])
        card_codes_str = ",".join(card_codes_list)
        return card_codes_str


class CardPile(object):
    """A pile of cards that we can use for various things"""
    def __init__(self, deck_id, pile_name, cards_to_add):
        pile = self.create_pile(deck_id, pile_name, cards_to_add)
        self.deck_id = deck_id
        self.name = pile_name
        self.remaining = pile['piles'][('{0}').format(self.name)]['remaining']

    def create_pile(self, deck_id, pile_name, cards_to_add):
        r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={cards_to_add}').format(
                deck_id = deck_id,
                pile = ('{player}').format(player = pile_name),
                cards_to_add = cards_to_add
                )
            )
        return r.json()

    def add_to_pile(self, cards_to_add):
        r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={cards_to_add}').format(
                deck_id = self.deck_id,
                pile = ('{player}').format(player = self.name),
                cards_to_add = cards_to_add
                )
            )
        self.remaining = r.json()['piles'][('{0}').format(self.name)]['remaining']        
    
    def get_card_codes_list(self):
        r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/list/').format(
                deck_id = self.deck_id,
                pile = ('{player}').format(player = self.name)
                )
            )
        cards = r.json()['piles'][('{0}').format(self.name)]['cards']
        card_codes_list = []
        for i in range(len(cards)):
            card_codes_list.append(cards[i]['code'])
        return card_codes_list

deck = Deck()
player_list = ['jenna', 'eddie', 'cp1', 'cp2', 'cp3']

jenna_pile = CardPile(deck.deck_id, 'jenna_draw', deck.draw_from_deck(4))


def init_game(deck, player_list):
    # create a card pile for each player to draw from
    # deals out even numbers to each player and then deals the rest of the deck
    initial_deal_card_num = int(52 / len(player_list))
    extra_cards_to_deal = 52 % len(player_list)
    pile_dict = {}
    for player in player_list:
        pile_dict[('{player}_draw_pile').format(player = player)] = CardPile(
            deck.deck_id, 
            ('{player}_draw_pile').format(player = player), 
            deck.draw_from_deck(initial_deal_card_num)
            )
    for i in range(extra_cards_to_deal):
        pile_dict[('{player}_draw_pile').format(player = player_list[i])].add_to_pile(deck.draw_from_deck(1))
    print('++++Game successfully initiated++++')
    return pile_dict


pile_dict = init_game(deck, player_list)

print(pile_dict)
print(pile_dict['jenna_draw_pile'].remaining)
# init not working properly yet


'''
print(jenna_pile.get_card_codes_list())
print(jenna_pile.name)
print(jenna_pile.deck_id)
print(jenna_pile.remaining)
'''