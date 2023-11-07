from cards import create_deck, deal_cards
from checks import check_hand

class CardGame:
    def __init__(self, num_players, num_cards_per_hand):
        self.deck = create_deck()
        self.num_players = num_players
        self.num_cards_per_hand = num_cards_per_hand

    def play_game(self):
        for i in range(self.num_players):
            player_hand = deal_cards(self.deck, self.num_cards_per_hand)
            hand_result = check_hand(player_hand)
            print(f"Player {i + 1} Hand: {player_hand}, Result: {hand_result}")

        print(f"Remaining cards in the deck: {len(self.deck)}")

if __name__ == "__main__":
    num_players = 5
    num_cards_per_hand = 5
    game = CardGame(num_players, num_cards_per_hand)
    game.play_game()
