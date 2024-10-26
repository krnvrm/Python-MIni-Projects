import os
import random 
import time
suits = ('Hearts','Diamonds','Clubs','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
#card class 
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+' of '+self.suit
#deck class
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        random.shuffle(self.deck)
    def deal_one(self):
        card = self.deck.pop()
        return card
    def __str__(self):
        x = ''
        for i in self.deck:
            x += str(i)+'\n'
        return x
    def __len__(self):
        return len(self.deck)
#player class
class Player():
    def __init__(self,deck):
        self.cards = []
        self.deck = deck
        self.chips = 100
    def disp_p_cards(self):
        for i in self.cards:
            print(i)
    def hit(self):
        x = self.deck.deal_one()
        self.cards.append(x)
    def __len__(self):
        return len(self.cards)
    def make_bet(self):
        x = 0
        while self.chips != 0:
            x=eval(input("How much do you want to bet ? "))
            if x > self.chips:
                print(f"You have {self.chips} chips left, so obviously you can't exceed that whilst making a bet")
            else:
                self.chips -= x 
                break
        else:
            print("You can't bet, you have 0 chips left !")
        return x 
    def clear_hand(self):
        self.cards.clear()
#dealer
class Dealer():
    def __init__(self,deck):
        self.cards = []
        self.deck = deck
    def hit(self):
        x = self.deck.deal_one()
        self.cards.append(x)
    def __len__(self):
        return len(self.cards)
    def clear_hand(self):
        self.cards.clear()
#game logic
def check_card_value(whochecks):
    if type(whochecks) == Dealer:
        x = 0 
        for i in whochecks.cards:
            x += values[i.rank]
        return x
    else:
        x = 0
        flag = False
        for i in whochecks.cards:
            if i.rank == 'Ace':
                flag = True
            x += values[i.rank]  
        if flag == True:
            if x-10 < 21:
                return (x-10)
            else:
                return(x)
        else:
            return(x)  
def print_dealer(dealer):
    if len(dealer) == 2: 
        x = 1
        for i in dealer.cards:
            if x == 1:
                print("<Card Hidden>")
            else:
                print(i)

            x += 1
    else:
        for i in dealer.cards:
            print(i)
def cards_on_table():
    global player,dealer 
    print("Dealer Cards Are :")
    print_dealer(dealer)
    print("Player Cards Are :")
    player.disp_p_cards()
def check_for_bust(x):
    if check_card_value(x)>21:
        return True
def check_for_win(bet):
    global player,dealer 
    dealer_value = check_card_value(dealer)
    player_value = check_card_value(player)
    if dealer_value <= 17 and player_value <= 21:
        if dealer_value > player_value:
            return ("The Dealer Won!",True)
        elif player_value > dealer_value:
            player.chips += bet*2
            return ("The Player Won!",True)
    elif dealer_value > 17:
        player.chips += bet*2
        return ("The Player Won!",True)
    elif player_value > 21:
        return ("The Dealer Won!",True)
def start_game():
    global player,dealer
    player.hit()
    player.hit()
    dealer.hit()
    dealer.hit()
deck = Deck()
player = Player(deck)
dealer = Dealer(deck)
while True:
    print("The Game Begins!")
    bet = player.make_bet()
    start_game()
    cards_on_table()
    while True:
        hitornaah = input("Do you wish to hit ? y/n ")
        flag = False
        if hitornaah.lower() == 'y':
            player.hit()
            os.system('cls')
            cards_on_table()
            if check_for_bust(player):
                print("BUST! You lost!")
                print(check_card_value(player))
                flag = True
                break
        else:
            break
    if not(flag):
        while True:
            dealer.hit()
            os.system('cls')
            cards_on_table()
            time.sleep(1)
            if check_card_value(dealer)>=17:
                break
        x = check_for_win(bet)
        print(x[0])
    ask = input("Wanna play again ? y/n ")
    if ask.lower() == 'y':
        player.clear_hand()
        dealer.clear_hand()
        deck.__init__()
    else:
        break
for i in range(5,0,-1):
    print(f'This will auto close in {i} secs')
    time.sleep(1) 
    os.system('cls')   