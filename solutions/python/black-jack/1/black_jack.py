
def value_of_card(card):
    if card is 'K' or card is 'J' or card is 'Q': return 10
    if card is 'A': return 1
    return int(card)

def higher_card(card_one, card_two):

    if value_of_card(card_one) > value_of_card(card_two): return card_one
    if value_of_card(card_one) < value_of_card(card_two): return card_two
    return card_one,card_two

def value_of_ace(card_one, card_two):
    if value_of_card(card_one)+value_of_card(card_two)>10 or card_one=='A' or card_two=='A': return 1
    return 11

def is_blackjack(card_one, card_two):
    if card_one==card_two: return False
    if (value_of_card(card_one)==1 or value_of_card(card_two)==1) and value_of_card(higher_card(card_one, card_two))==10: return True
    return False

def can_split_pairs(card_one, card_two):

    if value_of_card(card_one)==value_of_card(card_two): return True
    return False

def can_double_down(card_one, card_two):

    if value_of_card(card_one)+value_of_card(card_two)<12 and value_of_card(card_one)+value_of_card(card_two)>8: return True
    return False
