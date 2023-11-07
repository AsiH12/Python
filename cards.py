import itertools
import random

def create_deck():
    suits = "♥♦♣♠"
    values = "23456789TJQKA"
    return list(itertools.product(values, suits))

def deal_cards(deck, number):
    random.shuffle(deck)
    player_cards = [deck.pop() for i in range(number)]
    return player_cards
