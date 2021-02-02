# War game
# Takes Deck of Cards API and uses it to play simple card game

import requests

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


# Start up the game
    # ask for num players
    # get names for all players and assign them to player values
game_deck = Deck()
player_list = ['jenna', 'eddie', 'cp1', 'cp2', 'cp3', 'cp4']


def add_cards_to_player_draw_pile(deck, player, cards):
    # creates a card for a player from a deck and a player name string
    # draw proper number of cards from the deck for one player
    # the player's pile gets named 'player_pile' depending on the name given
    r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={cards}').format(
                deck_id = deck.deck_id,
                cards = str(cards)
                )
            )
    deck.remaining = deck.remaining - cards
    r_dict = r.json()
    player_cards = r_dict['cards']
    # takes dict card list and formats it to be added to pile
    player_card_codes_list = []
    for i in range(len(player_cards)):
        player_card_codes_list.append(player_cards[i]['code'])
    player_card_codes = ","
    player_card_codes = player_card_codes.join(player_card_codes_list)
    # put those cards into player's pile, API named 'player_pile'
    requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={player_card_codes}').format(
                deck_id = deck.deck_id,
                pile = ('{player}_pile').format(player = player),
                player_card_codes = player_card_codes
                )
            )


def init_game(deck, player_list):
    # create a card pile for each player to draw from
    # deals out even numbers to each player and then deals the rest of the deck
    initial_deal_card_num = int(52 / len(player_list))
    extra_cards = 52 % len(player_list)
    for player in player_list:
        add_cards_to_player_draw_pile(deck, player, initial_deal_card_num)
    for i in range(extra_cards):
        add_cards_to_player_draw_pile(deck, player_list[i], 1)
    print('++++Game successfully initiated++++')


def get_p_draw_card(deck, player):
    r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/draw/?count=1').format(
                deck_id = deck.deck_id,
                pile = ('{player}_pile').format(player = player)
                )
            )
    r_dict = r.json()
    player_cards = r_dict['cards']
    player_card_code = player_cards[0]['code']
    return player_card_code

def compare_cards(cards_list, player_list):
    # compares all the players' cards and returns the index of max
    # returns list of players who have max card val
    max_card_val = 0
    ind_list = []
    for i in range(len(cards_list)):
        card_str = cards_list[i][:-1]
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
    result = [player_list[i] for i in ind_list]
    return result

# called
def draw_cards_from_all_p_and_compare(deck, player_list):
    """ Takes in a deck and player_list, draws a card from each card and compares them
        to determine the highest value card. Returns a dict that contains a list of players
        with the highest card values, as well as the pot of cards they won
    """
    cards_to_compare = []
    for player in player_list:
        cards_to_compare.append(get_p_draw_card(deck, player))
    max_value_player_list = compare_cards(cards_to_compare, player_list)
    result_dict = {
        "max_value_player_list": max_value_player_list,
        "card_pot": cards_to_compare
    }
    return result_dict

def draw_all_cards_from_p_win_pile(deck, player, win_pile_count):
    # gets all remaining cards and puts them into codes string for proper insertion
    r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/draw/?count={all_cards}').format(
                deck_id = deck.deck_id,
                pile = ('{player}_win_pile').format(player = player),
                all_cards = int(win_pile_count)
                )
            )
    r_dict = r.json()
    player_cards = r_dict['cards']
    # takes dict card list and formats it to be added to pile
    player_card_codes_list = []
    for i in range(len(player_cards)):
        player_card_codes_list.append(player_cards[i]['code'])
    player_card_codes = ","
    player_card_codes = player_card_codes.join(player_card_codes_list)
    return player_card_codes

def transfer_cards_from_p_win_to_p_pile(deck, player, win_pile_count):
    # Take every card in player_win_pile and put it into player_pile
    cards_to_transfer = draw_all_cards_from_p_win_pile(deck, player, win_pile_count)
    # put those cards into player_pile
    requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={player_card_codes}').format(
                deck_id = deck.deck_id,
                pile = ('{player}_pile').format(player = player),
                player_card_codes = cards_to_transfer
                )
            )
    # then reshuffle player_pile
    requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/shuffle/').format(
                deck_id = deck.deck_id,
                pile = ('{player}_pile').format(player = player)
                )
            )

# called
def war_cleanup_function(deck, player_list):
    # war cleanup func repopulates proper piles for players still in the game
    # also returns list of players to remove
    # uses draw and transfer funcs to accomplish cleanup
    players_to_remove = []
    r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/list/').format(
                deck_id = game_deck.deck_id,
                pile = ('{player}_pile').format(player = player_list[0])
                )
            )
    r_dict = r.json()
    piles = r_dict['piles']
    for player in player_list:
        remaining = piles[('{player}_pile').format(player = player)]['remaining']
        print(('Remaining for {0}: {1}').format(player, remaining))
        try:
            win_pile_count = piles[('{player}_win_pile').format(player = player)]['remaining']
        except:
            win_pile_count = 0
        if remaining + win_pile_count < 2:
            print(("{player} does not have enough cards left! {player} is out of the game.").format(player = player))
            if win_pile_count > 0:
                transfer_cards_from_p_win_to_p_pile(game_deck, player, win_pile_count)
            players_to_remove.append(player)
        elif remaining < 2:
            transfer_cards_from_p_win_to_p_pile(game_deck, player, win_pile_count)
            print(("Cards transfered for {0}").format(player))
    return players_to_remove

def alter_player_list(players_to_remove):
    for player in players_to_remove:
        player_list.remove(player)

# called
def recursive_get_final_winner_and_pot(deck, result_dict):
    """ Takes in the result_dict from draw_cards_from_all_p_and_compare and continues to
        call the function until there's one winner in the max_value_player_list and
        the card pot is a cumulative of all the winnings
    """
    max_value_player_list = result_dict["max_value_player_list"]
    card_pot = result_dict["card_pot"]

    if len(max_value_player_list) > 1:
        if len(max_value_player_list) == 2:
            winners = " and ".join(max_value_player_list)
        else:
            winners = ", ".join(max_value_player_list)
        print(("There's a {tie_len}-way tie between {winners}!").format(
            tie_len = len(max_value_player_list),
            winners = winners
            )
        )
        print("This means War!")

        players_to_remove = war_cleanup_function(deck, max_value_player_list)
        if len(players_to_remove) > 0:
            for player in players_to_remove:
                card = get_p_draw_card(deck, player)
                result_dict["card_pot"] += card
                result_dict["max_value_player_list"].remove(player)
        alter_player_list(players_to_remove)

        if len(max_value_player_list) > 1:
            for player in max_value_player_list:
                card_pot += get_p_draw_card(deck, player)
            new_result_dict = draw_cards_from_all_p_and_compare(deck, max_value_player_list)
            new_result_dict["card_pot"] += card_pot
        else:
            return result_dict

        if len(new_result_dict["max_value_player_list"]) > 1:
            return recursive_get_final_winner_and_pot(deck, new_result_dict)
        else:
            return new_result_dict
    else:
        return result_dict

# called
def cards_to_player_win_pile(deck, winner, cards_won):
    # takes dict card list and formats it to be added to pile as string
    cards_won_codes = ","
    cards_won_codes = cards_won_codes.join(cards_won)
    # adding formatted cards to player_win_pile
    requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/add/?cards={player_card_codes}').format(
                deck_id = deck.deck_id,
                pile = ('{player}_win_pile').format(player = winner),
                player_card_codes = cards_won_codes
                )
            )

def eot_cleanup_function(deck, player_list):
    # end of turn func repopulates proper piles for players still in the game
    # also returns list of players to remove
    # uses draw and transfer funcs to accomplish cleanup
    players_to_remove = []
    # check if any player's player_pile is 0
    r = requests.get(
            ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/list/').format(
                deck_id = game_deck.deck_id,
                pile = ('{player}_pile').format(player = player_list[0])
                )
            )
    r_dict = r.json()
    piles = r_dict['piles']
    for player in player_list:
        remaining = piles[('{player}_pile').format(player = player)]['remaining']
        print(('Remaining for {0}: {1}').format(player, remaining))
        # if it's empty, transfer to player_pile
        if remaining == 0:
            try:
                win_pile_count = piles[('{player}_win_pile').format(player = player)]['remaining']
                if win_pile_count == 0:
                    print(("{player} has no cards left! {player} is out of the game.").format(player = player))
                    players_to_remove.append(player)
                else:
                    transfer_cards_from_p_win_to_p_pile(game_deck, player, win_pile_count)
                    print(("Cards transfered for {0}").format(player))
            except:
                print(("{player} has no cards left! {player} is out of the game.").format(player = player))
                players_to_remove.append(player)
    return players_to_remove

# calls all of the above labeled functions
def take_a_turn(game_deck, player_list):
    print(("Turn starting player list: {0}").format(player_list))

    d = draw_cards_from_all_p_and_compare(game_deck, player_list)

    final = recursive_get_final_winner_and_pot(game_deck, d)

    winner = final["max_value_player_list"][0]
    card_pot = final["card_pot"]

    cards_to_player_win_pile(game_deck, winner, card_pot)
    print(("{winner} won all of the cards!").format(winner = winner))

    players_to_remove = eot_cleanup_function(game_deck, player_list)
    if len(players_to_remove) > 0:
        alter_player_list(players_to_remove)

def main():
    init_game(game_deck, player_list)

    count = 1
    while len(player_list) > 1:
        r = requests.get(
                ('https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile}/list/').format(
                    deck_id = game_deck.deck_id,
                    pile = ('{player}_win_pile').format(player = 'jenna')
                    )
                )
        take_a_turn(game_deck, player_list)
        print('Turn completed: ' + str(count))
        count += 1
    else:
        print(("Congrats {player}! You've won the game!").format(player = player_list[0]))

    # print(r.text)

if __name__ == "__main__":
    main()
