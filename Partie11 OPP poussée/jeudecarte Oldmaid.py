

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0

    def __eq__(self, other):
        # equality
        return self.cmp(other) == 0

    def __le__(self, other):
        # less than or equal
        return self.cmp(other) <= 0

    def __ge__(self, other):
        # greater than or equal
        return self.cmp(other) >= 0

    def __gt__(self, other):
        # strictly greater than
        return self.cmp(other) > 0

    def __lt__(self, other):
        # strictly less than
        return self.cmp(other) < 0

    def __ne__(self, other):
        # not equal
        return self.cmp(other) != 0


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s,spaces = "",""
        for c in self.cards:
            s = s + spaces + str(c) + "\n"
            spaces += " "
        return s

    def shuffle(self):
        import random
        rng = random.Random()        # Create a random generator
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i, num_cards)
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    def shuffle2(self):
        import random
        rng = random.Random()        # Create a random generator
        rng.shuffle(self.cards)      # Use its shuffle method

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=None):
        if num_cards==None :             # if no default value given for how many cards to deal
            num_cards = len(self.cards)  # then deal all cards in the deck
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class Hand(Deck):

    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
            return s
        else:
            s += " contains\n"
            return s + super().__str__()    # super call by making use of the super() function (preferred)

    def add(self, card):
        self.cards.append(card)
        return self


class OldMaidHand(Hand):

    def remove_matches(self):
        count = 0                               # counts number of matches that have been removed
        original_cards = self.cards.copy()      # makes a copy of the original set of cards in your hand
        for card in original_cards:             # iterate over all cards in your hand
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:             # if the matching card is in your hand
                self.cards.remove(card)         # remove the card from your hand
                self.cards.remove(match)        # remove the match from your hand
                count += 1                      # add one to the count of matches that have been removed
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
        return count                            # return number of matches that have been removed


class OldMaidGame(CardGame):

    def play(self, names):
        # Remove Queen of Clubs
        queen_clubs = Card(0,12)
        self.deck.remove(queen_clubs)

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        print("---------- Discarding matches from hands")
        matches = self.remove_all_matches()
        print("---------- Matches have been discarded")
        self.print_hands()

        # Play until all 50 cards are matched
        # in other words, until 25 pairs have been matched
        print("---------- Play begins")
        turn = 0
        num_players = len(names)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_players

        print("---------- Game is Over")
        self.print_hands()

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        print("Player" + str(i) + ":")
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor
            
            
OldMaidGame().play(["kim","charles","siegfried"])