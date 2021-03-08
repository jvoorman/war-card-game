# War game
# Takes Deck of Cards API and uses it to play simple card game

import requests

class Deck(object):
    """This is the deck that we're gonna use for our card game"""
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
            f'https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={str(num_cards)}'
            )
        cards = r.json()['cards']
        card_codes_list = [card['code'] for card in cards]
        card_codes_str = ",".join(card_codes_list)
        self.remaining -= num_cards
        return card_codes_str

class CardPile(object):
    """A pile of cards that we can use for various things"""
    def __init__(self, deck_id, pile_name, cards_to_add):
        pile = self.create_pile(deck_id, pile_name, cards_to_add)
        self.pile = pile
        self.deck_id = deck_id
        self.name = pile_name
        self.remaining = pile['piles'][f'{self.name}']['remaining']

    def create_pile(self, deck_id, pile_name, cards_to_add):
        r = requests.get(
            f'https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/add/?cards={cards_to_add}'
            )
        return r.json()

    def add_to_pile(self, cards_to_add):
        r = requests.get(
            f'https://deckofcardsapi.com/api/deck/{self.deck_id}/pile/{self.name}/add/?cards={cards_to_add}'
            )
        self.remaining = r.json()['piles'][f'{self.name}']['remaining']        
    
    def get_card_codes_list(self):
        r = requests.get(
            f'https://deckofcardsapi.com/api/deck/{self.deck_id}/pile/{self.name}/list/'
            )
        cards = r.json()['piles'][f'{self.name}']['cards']
        card_codes_list = [card['code'] for card in cards]
        return card_codes_list

    def draw_cards_from_top_of_pile(self, num_cards):
        r = requests.get(
            f'https://deckofcardsapi.com/api/deck/{self.deck_id}/pile/{self.name}/draw/?count={num_cards}'
            )
        self.remaining = r.json()['piles'][f'{self.name}']['remaining']
        cards = r.json()['cards']
        card_codes_list = [card['code'] for card in cards]
        card_codes_str = ",".join(card_codes_list)
        return card_codes_str
    
    def shuffle_pile(self):
        requests.get(
            f'https://deckofcardsapi.com/api/deck/{self.deck_id}/pile/{self.name}/shuffle'
            )

class PilePile(object):
    """This is the dict of CardPiles that can perform game operations"""
    def __init__(self, deck_id):
        pile_dict = {}
        self.pile_dict = pile_dict
        self.deck_id = deck_id

    def add_pile(self, card_pile):
        self.pile_dict[card_pile.name] = card_pile
    
    def get_pile(self, pile_name):
        return self.pile_dict.get(pile_name)
    
    def pile_to_pile_transfer(self, from_pile_name, to_pile_name):
        # gets all cards from_pile and puts them into codes string for proper insertion
        from_pile = self.get_pile(from_pile_name)
        cards_to_transfer = from_pile.draw_cards_from_top_of_pile(from_pile.remaining)
        try:
            to_pile = self.get_pile(to_pile_name)
            to_pile.add_to_pile(cards_to_transfer)
        except:
            self.add_pile(CardPile(self.deck_id, to_pile_name, cards_to_transfer))

def war_function(player_list, pile_pile):
    """Recursive function that decides the winner when War has to happen"""
    # draw cards from all player_piles to compare
    cards_to_compare = []
    for player in player_list:
        player_pile = pile_pile.get_pile(f'{player}_draw')
        card = player_pile.draw_cards_from_top_of_pile(1)
        cards_to_compare.append(card)
    # compares all the players' cards
    max_card_val = 0
    ind_list = []
    for i in range(len(cards_to_compare)):
        card_str = cards_to_compare[i][:-1]
        card_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '0': 10}
        if card_str in card_dict:
            card_val = card_dict[card_str]
        else:
            card_val = int(card_str)
        if card_val > max_card_val:
            max_card_val = card_val
            ind_list = [i]
        elif card_val == max_card_val:
            ind_list.append(i)
    max_value_player_list = [player_list[i] for i in ind_list]
    # put cards into card_pot
    try:
        card_pot = pile_pile.get_pile('card_pot')
        card_pot.add_to_pile(",".join(cards_to_compare))
    except:
        card_pot = CardPile(pile_pile.deck_id, 'card_pot', ",".join(cards_to_compare))
        pile_pile.add_pile(card_pot)
    for player in player_list:
        player_pile = pile_pile.get_pile(f'{player}_draw')
        card = player_pile.draw_cards_from_top_of_pile(1)
        card_pot.add_to_pile(card)
    # handle War scenario
    if len(max_value_player_list) > 1:
        if len(max_value_player_list) == 2:
            winners = " and ".join(max_value_player_list)
        else:
            winners = ", ".join(max_value_player_list)
        print(f"There's a {len(max_value_player_list)}-way tie between {winners}!")
        print("This means War again!")

        # clean up piles and remove appropriate players for War
        players_to_remove = []
        for player in max_value_player_list:
            player_draw_pile = pile_pile.get_pile(f'{player}_draw')
            try:
                player_win_pile = pile_pile.get_pile(f'{player}_win')
                win_pile_count = player_win_pile.remaining
            except:
                win_pile_count = 0
            if win_pile_count + player_draw_pile.remaining < 2:
                print(f"{player} does not have enough cards left! {player} is out of the game.")
                # all player cards need to go into card_pot so make sure they're all in draw pile
                if win_pile_count > 0:
                    pile_pile.pile_to_pile_transfer(f'{player}_win', f'{player}_draw')
                players_to_remove.append(player)
            elif player_draw_pile.remaining < 2:
                pile_pile.pile_to_pile_transfer(f'{player}_win', f'{player}_draw')
        if len(players_to_remove) > 0:
            if len(players_to_remove) == len(max_value_player_list):
                print('Whoops, looks like War isn\'t gonna happen.')
                print('Since it\'s way too much work to create a real solution, first player wins.')
                players_to_remove = players_to_remove[1:]
            for player in players_to_remove:
                pile_pile.pile_to_pile_transfer(f'{player}_draw', 'card_pot')
                max_value_player_list.remove(player)

        if len(max_value_player_list) > 1:
            winner = war_function(max_value_player_list, pile_pile)
        else:
            winner = max_value_player_list[0]
    else:
        winner = max_value_player_list[0]
    # give cards to turn winner
    pile_pile.pile_to_pile_transfer('card_pot', f'{winner}_win')
    print(f"{winner} has the higher card!")
    return winner

def take_a_turn(player_list, pile_pile):
    """Takes in a Pilepile and player_list and performs all necessary functions to take a turn"""
    # draw cards from all player_piles to compare
    cards_to_compare = []
    for player in player_list:
        player_pile = pile_pile.get_pile(f'{player}_draw')
        card = player_pile.draw_cards_from_top_of_pile(1)
        cards_to_compare.append(card)
    # compares all the players' cards
    max_card_val = 0
    ind_list = []
    for i in range(len(cards_to_compare)):
        card_str = cards_to_compare[i][:-1]
        card_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '0': 10}
        if card_str in card_dict:
            card_val = card_dict[card_str]
        else:
            card_val = int(card_str)
        if card_val > max_card_val:
            max_card_val = card_val
            ind_list = [i]
        elif card_val == max_card_val:
            ind_list.append(i)
    max_value_player_list = [player_list[i] for i in ind_list]
    # put cards into card_pot
    try:
        card_pot = pile_pile.get_pile('card_pot')
        card_pot.add_to_pile(",".join(cards_to_compare))
    except:
        card_pot = CardPile(pile_pile.deck_id, 'card_pot', ",".join(cards_to_compare))
        pile_pile.add_pile(card_pot)
    # handle War scenario
    if len(max_value_player_list) > 1:
        if len(max_value_player_list) == 2:
            winners = " and ".join(max_value_player_list)
        else:
            winners = ", ".join(max_value_player_list)
        print(f"There's a {len(max_value_player_list)}-way tie between {winners}!")
        print("This means War!")

        # clean up piles and remove appropriate players for War
        players_to_remove = []
        for player in max_value_player_list:
            player_draw_pile = pile_pile.get_pile(f'{player}_draw')
            try:
                player_win_pile = pile_pile.get_pile(f'{player}_win')
                win_pile_count = player_win_pile.remaining
            except:
                win_pile_count = 0
            if win_pile_count + player_draw_pile.remaining < 2:
                print(f"{player} does not have enough cards left! {player} is out of the game.")
                # all player cards need to go into card_pot so make sure they're all in draw pile
                if win_pile_count > 0:
                    pile_pile.pile_to_pile_transfer(f'{player}_win', f'{player}_draw')
                players_to_remove.append(player)
            elif player_draw_pile.remaining < 2:
                pile_pile.pile_to_pile_transfer(f'{player}_win', f'{player}_draw')
        if len(players_to_remove) > 0:
            if len(players_to_remove) == len(max_value_player_list):
                print('Whoops, looks like War isn\'t gonna happen.')
                print('Since it\'s way too much work to create a real solution, first player wins.')
                players_to_remove = players_to_remove[1:]
            for player in players_to_remove:
                pile_pile.pile_to_pile_transfer(f'{player}_draw', 'card_pot')
                max_value_player_list.remove(player)

        if len(max_value_player_list) > 1:
            winner = war_function(max_value_player_list, pile_pile)
        else:
            winner = max_value_player_list[0]
    else:
        winner = max_value_player_list[0]
    # give cards to turn winner
    pile_pile.pile_to_pile_transfer('card_pot', f'{winner}_win')
    print(f"{winner} won all of the cards!")

def main():
    # initiate the game, dealing out all cards
    game_deck = Deck()
    player_count = input('How many players would you like to play with? \n> ')
    while True:
        try:
            assert(player_count.isnumeric())
            assert(0 < int(player_count) < 52)
            break
        except:
            player_count = input('I\'m sorry, please enter an appropriate number of players. \n> ')
    player_list = []
    for i in range(int(player_count)):
        new_player = input(f'What is the name of player {i + 1}? \n> ')
        while not new_player.replace(' ', '').isalnum():
            new_player = input('I\'m sorry, please enter a more API-friendly player name. \n> ')
        player_list.append(new_player)
    turn_limit = input('How many turns before you give up? \n> ')
    while True:
        try:
            assert(turn_limit.isnumeric())
            assert(0 < int(turn_limit))
            break
        except:
            turn_limit = input('C\'mon, get your stuff together and give me some good input. \n> ')
    initial_deal_card_num = int(52 / len(player_list))
    extra_cards_to_deal = 52 % len(player_list)
    pile_pile = PilePile(game_deck.deck_id)
    for player in player_list:
        extra_cards = 0
        if extra_cards_to_deal > 0:
            extra_cards = 1
            extra_cards_to_deal -= 1
        pile_name = f'{player}_draw'
        cards_to_add = game_deck.draw_from_deck(initial_deal_card_num + extra_cards)
        pile_pile.add_pile(CardPile(game_deck.deck_id, pile_name, cards_to_add))
    print('++++Game successfully initiated++++')
    # continue to take turns until only one player is left
    turn_count = 1
    while turn_count <= int(turn_limit):
        print(f"---------------------------------")
        # clean up piles and remove appropriate players
        players_to_remove = []
        for player in player_list:
            player_draw_pile = pile_pile.get_pile(f'{player}_draw')
            try:
                player_win_pile = pile_pile.get_pile(f'{player}_win')
                win_pile_count = player_win_pile.remaining
            except:
                win_pile_count = 0
            total_cards = player_draw_pile.remaining + win_pile_count
            print(f'Total cards for {player}: {total_cards}')
            if player_draw_pile.remaining == 0:
                if win_pile_count == 0:
                    print(f"{player} has no cards left! {player} is out of the game.")
                    players_to_remove.append(player)
                else:
                    pile_pile.pile_to_pile_transfer(f'{player}_win', f'{player}_draw')
                    player_draw_pile.shuffle_pile()
        if len(players_to_remove) > 0:
            for player in players_to_remove:
                player_list.remove(player)
                
        if len(player_list) < 2:
            print(f"Congrats {player_list[0]}! You've won the game!")
            break
        else:
            print(f"Taking turn...") 
            take_a_turn(player_list, pile_pile)

            print(f'Turn completed: {str(turn_count)}')
            turn_count += 1
    else:
        print('Out of turns, Game Over')

if __name__ == "__main__":
    main()
