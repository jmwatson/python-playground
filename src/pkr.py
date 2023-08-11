from flask import Flask, request

app = Flask(__name__)

# defining these as constants in the case we need to change these in the future.
# that will allow us to change the value here instead of multiple places in code.
STRAIGHT_FLUSH = 500
THREE_OF_A_KIND = 400
FLUSH = 300
STRAIGHT = 200
PAIR = 100

# Logic section
def ace_low_rank(card):
    return 'A23456789'.index(card[0])

def rank(card):
    # to keep the indexes matching with the Ace low rankings then we need the blank space at the beginning
    return ' 23456789A'.index(card[0])

def is_straight(cards):
    ranks = sorted(ace_low_rank(card) for card in cards)
    return len(set(ranks)) == 3 and ranks[2] - ranks[0] == 2

def is_flush(cards):
    return all(card[1] == cards[0][1] for card in cards)

def hand_rank(cards):

    # Straight Flush
    if is_straight(cards) and is_flush(cards):
        return STRAIGHT_FLUSH + max([ace_low_rank(card) for card in cards])
    
    # Straight
    if is_straight(cards):
        return STRAIGHT_FLUSH + max([ace_low_rank(card) for card in cards])
    
    # Flush
    if is_flush(cards):
        return FLUSH + max([rank(card) for card in cards])
    
    # only calculating this after we have ruled out a straight flush or a straight or a flush
    # since those don't rely on counting how many ranks are in a hand
    hand_ranks = [card[0] for card in cards]
    counts = [hand_ranks.count(card) for card in hand_ranks]

    # Three of a kind
    if 3 in counts:
        return THREE_OF_A_KIND + max([rank(card) for card in cards])
    
    # Pair
    if 2 in counts:
        pair_rank = max([rank(card) for card in cards if cards.count(card) == 2])
        return PAIR + pair_rank
    
    # High card
    return max([rank(card) for card in cards])

def compare(hand1, hand2):
    rank1 = hand_rank(hand1)
    rank2 = hand_rank(hand2)

    if rank1 != rank2:
        return 1 if rank1 > rank2 else 2
    
    # sort in descending order
    hand1.sort(key=lambda card: -rank(card))
    hand2.sort(key=lambda card: -rank(card))

    # compare the now sorted cards if the hands have the same high card for the first difference in ranks
    for card1, card2 in zip(hand1, hand2):
        if rank(card1) != rank(card2):
            return 1 if rank(card1) > rank(card2) else 2
        
    return 0

# Flask endpoints

# The request data will be formatted to look like this
# {
#     'hand1': ['AH', '7C', '8D'],
#     'hand2': ['9C', '7D', '8C']
# }
@app.route('/compare-hands', methods=['POST'])
def compare_hands_endpoint():
    data = request.json
    hand1 = data['hand1']
    hand2 = data['hand2']

    result = compare(hand1, hand2)

    if result == 1:
        return {'result': 'Hand 1 wins!'}, 200
    elif result == 2:
        return {'result': 'Hand 2 wins!'}, 200
    else:
        return {'result': "It's a tie!"}, 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)