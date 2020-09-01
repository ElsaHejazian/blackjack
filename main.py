import random
import os


deck_cards = {"2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5,
              "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9, "10 of Diamonds": 10,
              "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10, "Ace of Diamonds": 11,
              "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5,
              "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10,
              "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10, "Ace of Spades": 11,
              "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5,
              "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9, "10 of Hearts": 10,
              "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10, "Ace of Hearts": 11,
              "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5,
              "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9, "10 of Clubs": 10,
              "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10, "Ace of Clubs": 11,
              }


def make_deck():
    global player_hand_name
    global player_hand_value
    global computer_hand_name
    global computer_hand_value
    global deck_cards
    deck_cards = {"2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4, "5 of Diamonds": 5,
                  "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8, "9 of Diamonds": 9, "10 of Diamonds": 10,
                  "Jack of Diamonds": 10, "Queen of Diamonds": 10, "King of Diamonds": 10, "Ace of Diamonds": 11,
                  "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4, "5 of Spades": 5,
                  "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8, "9 of Spades": 9, "10 of Spades": 10,
                  "Jack of Spades": 10, "Queen of Spades": 10, "King of Spades": 10, "Ace of Spades": 11,
                  "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4, "5 of Hearts": 5,
                  "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8, "9 of Hearts": 9, "10 of Hearts": 10,
                  "Jack of Hearts": 10, "Queen of Hearts": 10, "King of Hearts": 10, "Ace of Hearts": 11,
                  "2 of Clubs": 2, "3 of Clubs": 3, "4 of Clubs": 4, "5 of Clubs": 5,
                  "6 of Clubs": 6, "7 of Clubs": 7, "8 of Clubs": 8, "9 of Clubs": 9, "10 of Clubs": 10,
                  "Jack of Clubs": 10, "Queen of Clubs": 10, "King of Clubs": 10, "Ace of Clubs": 11,
                  }
    computer_hand_name = []
    computer_hand_value = []
    player_hand_name = []
    player_hand_value = []


computer_hand_name = []
computer_hand_value = []
player_hand_name = []
player_hand_value = []
player_bet = 0
ace_card = None


def start_hands():
    global player_hand_name
    global player_hand_value

    # computer starting hand
    y = random.choice(list(deck_cards.items()))
    computer_hand_name.append(y[0])
    computer_hand_value.append(y[1])
    del deck_cards[y[0]]

    # player starting hand
    for i in range(0, 2):
        x = random.choice(list(deck_cards.items()))
        player_hand_name.append(x[0])
        player_hand_value.append(x[1])
        del deck_cards[x[0]]


class Account:
    def __init__(self, money):
        self.money = money

    def win(self):
        self.money += player_bet

    def lose(self):
        self.money -= player_bet


player_account = Account(0)


def charge():
    global player_account
    while True:
        try:
            paid = int(input("How much dollars do you want to charge your account:"))
        except ValueError:
            print("Sorry! Please enter valid input:")
            continue
        if paid <= 0:
            print("Sorry! Please enter positive integer.")
            continue
        else:
            player_account.money = paid
            break


def bet_money():
    global player_bet
    while True:
        try:
            bet = int(input("How much do you want to bet:"))
        except ValueError:
            print("Sorry, please enter valid input.")
            continue
        if bet > player_account.money:
            print("Sorry! You don't have enough money.")
            continue
        elif bet <= 0:
            print("Sorry! Please enter positive integer.")
            continue
        else:
            player_bet = bet
            break


def check_for_bust():
    global playing
    global player_hand_value
    global ace_card
    ace = False
    for card in range(0, len(player_hand_value)):
        if player_hand_value[card] == 11:
            ace = True
            ace_card = card
            break
    if sum(player_hand_value) == 21:
        playing = False
    elif sum(player_hand_value) >= 21 and not ace:
        playing = False
    elif sum(player_hand_value) >= 21 and ace:
        player_hand_value[ace_card] = 1


def check_for_winner():
    global player_hand_value
    global computer_hand_value

    if sum(player_hand_value) > 21 or sum(player_hand_value) < sum(computer_hand_value):
        print("Sorry! You lose!")
        player_account.lose()
    else:
        print("Congratulations! You won!")
        player_account.win()


playing = True


def turn_handle():
    global playing
    while True:
        asking = input("Do you want to hit or stay?")
        if asking.lower() == "hit":
            x = random.choice(list(deck_cards.items()))
            player_hand_name.append(x[0])
            player_hand_value.append(x[1])
            del deck_cards[x[0]]
            check_for_bust()
            break
        elif asking.lower() == "stay":
            y = random.choice(list(deck_cards.items()))
            computer_hand_name.append(y[0])
            computer_hand_value.append(y[1])
            del deck_cards[y[0]]
            playing = False
            break
        else:
            print("Please enter hit or stay.")


def clear():
    os.system('cls')


def printing():
    print(f"Your hand is: {player_hand_name}")
    print(f"The host hand is: {computer_hand_name}")
    print(f"You have {player_account.money}$ in your account.")


clear()
charge()


def play_game():
    global playing
    play_again = True
    while play_again:
        clear()
        playing = True
        start_hands()
        bet_money()
        check_for_bust()
        while playing:
            clear()
            printing()
            turn_handle()
        clear()
        check_for_winner()
        printing()
        if player_account.money == 0:
            print("Sorry! You lose all of your money.")
            play_again = False
        else:
            while True:
                ask_for_rematch = input("Do you want to play again?")
                if ask_for_rematch.lower() == "yes":
                    make_deck()
                    break
                elif ask_for_rematch.lower() == "no":
                    play_again = False
                    break
                else:
                    print("Please enter yes or no.")


play_game()
