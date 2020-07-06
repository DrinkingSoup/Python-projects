
import cards

# Create the deck of cards

the_deck = cards.Deck()
the_deck.shuffle()

#Deal out cards
player1_list = []
player2_list = []
for i in range(5):
    player1_list.append(the_deck.deal())
    player2_list.append(the_deck.deal())



#Battle the cards

Battle = True
while Battle:
    print("Hand 1: ", player1_list)
    print("Hand 2: ", player2_list)

    if len(player1_list) != 0 and len(player2_list) != 0:
        player1_card = player1_list.pop(0)
        player2_card = player2_list.pop(0)

        if player1_card.rank() > player2_card.rank():
            print(f"Battle was {player1_card} to {player2_card}, Player 1 Wins Battle")
            player1_list.append(player1_card)
            player1_list.append(player2_card)
        elif player1_card.rank() < player2_card.rank():
            print(f"Battle was {player1_card} to {player2_card}, Player 2 Wins Battle")
            player2_list.append(player1_card)
            player2_list.append(player2_card)
        else:
            print(f"Battle was {player1_card} to {player2_card}, Battle is tied")
            player1_list.append(player1_card)
            player2_list.append(player2_card)

        user_input = input("Keep going? (y/n)")

        if user_input.lower() == "n":
            if len(player1_list) > len(player2_list):
                print("Player 1 Wins!")
            elif len(player1_list) < len(player2_list):
                print("Player 2 Wins!")
            else:
                print("Tie!")
            Battle = False
    elif len(player1_list) == 0:
        print("Player 2 Wins!")
        Battle = False
    elif len(player2_list) == 0:
        print("Player 1 Wins!")
        Battle = False
    else:
        print("Tie!")
        Battle = False


