from __future__ import print_function
from rdoclient import RandomOrgClient
r=RandomOrgClient("0c39b793-4783-42d1-ae19-c465c076fa9b")
win1=0
win2=0
print("We are going to play a game called dice duels! Dice duels is a game where two players participate in rolling dice. The first player rolls and then the second, whoever\nhas the higher roll wins that round. It's a best of three games so whoever wins two rounds first wins the game.")
player1=str(raw_input("Enter Player 1's name: "))
player2=str(raw_input("Enter player 2's name: "))
while(win1!=2 and win2!=2):
	roll1=r.generate_integers(1,1,6)
	output1=roll1[0]
	player1roll=raw_input("{} type roll to roll!\n>".format(player1))
	while(player1roll!="roll"):
		player1roll=raw_input("{} type roll to roll!\n>".format(player1))
	print("{} got {}.".format(player1,output1))
	roll2=r.generate_integers(1,1,6)
	output2=roll2[0]
	player2roll=raw_input("{} type roll to roll!\n>".format(player2))
	while(player2roll!="roll"):
		player2roll=raw_input("{} type roll to roll!\n>".format(player2))
	print("{} got {}.".format(player2,output2))
	if(roll1>roll2):
		print("Nice, {} one this round!".format(player1))
		win1+=1
		print("The score is {} to {}.".format(win1,win2))
	if(roll1<roll2):
		print("Nice, {} one this round!".format(player2))
		win2+=1
		print("The score is {} to {}.".format(win1,win2))
	if(roll1==roll2):
		print("Both players rolled the same number, this round does not count for either player.")
if(win1>win2):
	print("Congrats! {} won the game with a score of {} to {}".format(player1,win1,win2))
else:
	print("Congrats! {} won the game with a score of {} to {}.".format(player2,win2,win1))

#Hello Mr.Gold
#I need more commits
#I don't know how to do true random so pls let me KNOW!!!
