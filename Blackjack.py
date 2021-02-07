from random import randint
class card():
    def __init__(self, suit, value):
        self.suit=suit
        self.value=value

class deck():    
    def __init__(self):
        self.cards=[]
        self.suits=["Spades", "Clubs", "Diamonds", "Hearts"]
        self.values=[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.remake_deck()
    def remake_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(card(suit, value))
    def deal(self):
        dealt = self.cards[randint(0, len(self.cards))]
        self.cards.remove(dealt)
        return dealt

class player():
    player_type = "Blackjack player"
    def __init__self(self, name):
        self.name=name
        self.hand=[]
        self.bust=False
        self.blackjack=False
    def change_name(self, new_name):
        self.name=new_name
    def take_card(self, new_card):
        if not self.bust:
            self.hand.append(new_card)
        return self.calculate_hand
    def calculate_hand(self):
        total=0
        for card in self.hand:
            if card.value in ["Jack", "Queen", "King"]:
                total += 10
            elif card.value != "Ace":
                total += card.value
        num_aces=0
        for card in self.hand:
            if card.value == "Ace":
                num_aces += 1
        if total+num_aces-1<=10:
            total+=(11+num_aces-1)
        else:
            total+=num_aces
        if total>21:
            self.bust=True
    def get_player_type(self):
        return self.player_type

def startGame(numPlayers):
    current_deck = deck()
    players = []
    for num in range(1, numPlayers+1):
        players.append(player(input("Enter name for player {}".format(num))))
    for num in range(0, num_players):
        players[num].take_card(current_deck.deal())