from classes.deck import Deck
import random

bicycle = Deck()

# bicycle.show_cards()

player1 = []
player2 = []
random.shuffle(bicycle.cards)
# bicycle.show_cards()
for i in range (0,26):
    player1.append(bicycle.cards[i])

for i in range (26,52):
    player2.append(bicycle.cards[i])

# for i in range (0,len(player1)):
#     player1[i].card_info()

# # print("this is the start of plyr 2hand")
# for i in range (0,len(player2)):
#     player2[i].card_info()

#player1 and player2 pop off top card compare larger value keeps both cards
print("Let's play war!")
char=input("Press s to start and any other key to quit game")

reward = []
while len(player1) > 0 and len(player2) > 0 and char == "s":
    val1 = player1.pop()
    val2 = player2.pop()
    print(f"player1's card is {val1.string_val} and player2's card is {val2.string_val}")
    if val1.point_val == val2.point_val:
        reward.append(val1)
        reward.append(val2)
        print("both cards are equal")
    elif val1.point_val > val2.point_val:
        print("player1 has the higher value")
        player1.append(val1)
        player1.append(val2)
        while (len(reward)>0):
            player1.append(reward.pop())
    elif val1.point_val < val2.point_val:
        print("player2 has the higher value")
        player2.append(val1)
        player2.append(val2)
        while (len(reward)>0):
            player2.append(reward.pop())
    print(f"player1 has {len(player1)} cards")
    print(f"player2 has {len(player2)} cards")
    char=input("Press s to flip a card")
if len(player1) == len(player2):
    print("Tie!")
elif len(player1) < len(player2):
    print("player2 wins!")
else:
    print("player1 wins!")

# print(len(player1))
# print(len(player2))