
from random import randint
player1=raw_input("Enter player 1's name: ")
player2=raw_input("\nEnter player 2's name: ")
win1=0
win2=0
print("\nWe are going to play a game called Dice Duels, except with different rules. Hint, There will be an easter egg can you find it? Remember,\n\nthe lower number wins over the bigger number, and each player will roll three dye per turn.")
while(win1!=3 and win2!=3):
	player1roll=raw_input("\n{} type roll to roll three dye.\n>".format(player1))
	while(player1roll!="roll" and player1roll!="Brendan is awesome"):
			player1roll=raw_input("\n{} type roll to roll three dye.\n>".format(player1))
	roll1=[randint(1,6),randint(1,6),randint(1,6)]
	print("\n{} rolled {}.".format(player1,roll1))
	player2roll=raw_input("\n{} type roll to roll three dye.\n>".format(player2))
	while(player2roll!="roll" and player2roll!="Brendan is awesome"):
		player2roll=raw_input("\n{} type roll to roll three dye. \n>".format(player2))
	roll2=[randint(1,6),randint(1,6),randint(1,6)]
	print("\n{} rolled {}.".format(player2,roll2))
	if(roll1[0]>roll1[1] and roll1[0]>roll1[2]):
		high1=roll1[0]
	if(roll1[0]<roll1[1] and roll1[0]<roll1[2]):
		low1=roll1[0]
	if(roll1[0]>roll1[1] and roll1[0]<roll1[2]):
		mid1=roll1[0]
	if(roll1[0]<roll1[1] and roll1[0]>roll1[2]):
		mid1=roll1[0]


	if(roll1[1]>roll1[0] and roll1[1]> roll1[2]):
		high1=roll1[1]
	if(roll1[1]<roll1[0] and roll1[1]<roll1[2]):
		low1=roll1[1]
	if(roll1[1]>roll1[0] and roll1[1]<roll1[2]):
		mid1=roll1[1]
	if(roll1[1]<roll1[0] and roll1[1]>roll1[2]):
		mid1=roll1[1]

	if(roll1[1]==roll1[0] and roll1[0]>roll1[2]):
		high1=roll1[1]
		mid1=roll1[0]
	if(roll1[1] == roll1[0] and roll1[0]<roll1[2]):
		low1=roll1[0]
		mid1=roll1[1]

	if(roll1[1]==roll1[2] and roll1[2]>roll1[0]):
		high1=roll1[1]
		mid1=roll1[2]
	if(roll1[1] == roll1[2] and roll1[2]<roll1[0]):
		low1=roll1[2]
		mid1=roll1[1]
	if(roll1[2]==roll1[0] and roll1[0]>roll1[1]):
		high1=roll1[2]
		mid1=roll1[0]
	if(roll1[2] == roll1[0] and roll1[2]<roll1[1]):
		low1=roll1[0]
		mid1=roll1[2]
	





	if(roll1[2]>roll1[0] and roll1[2]>roll1[1]):
		high1=roll1[2]
	if(roll1[2]<roll1[0] and roll1[2]<roll1[1]):
		low1=roll1[2]
	if(roll1[2]>roll1[0] and roll1[2]<roll1[1]):
		mid1=roll1[2]
	if(roll1[2]<roll1[0] and roll1[2]>roll1[1]):
		mid1=roll1[2]
	if(roll1[0]==roll1[1] and roll1[0]==roll1[2]):
		high1=roll1[0]
		mid1=roll1[1]
		low1=roll1[2]
	print("\n\nFor {}, the high number is {}, the middle number is {}, and the lowest number is {}.".format(player1,high1,mid1,low1))
	if(roll2[0]>roll2[1] and roll2[0]>roll2[2]):
		high2=roll2[0]
	if(roll2[0]<roll2[1] and roll2[0]<roll2[2]):
		low2=roll2[0]
	if(roll2[0]>roll2[1] and roll2[0]<roll2[2]):
		mid2=roll2[0]
	if(roll2[0]<roll2[1] and roll2[0]>roll2[2]):
		mid2=roll2[0]


	if(roll2[1]>roll2[0] and roll2[1]> roll2[2]):
		high2=roll2[1]
	if(roll2[1]<roll2[0] and roll2[1]<roll2[2]):
		low2=roll2[1]
	if(roll2[1]>roll2[0] and roll2[1]<roll2[2]):
		mid2=roll2[1]
	if(roll2[1]<roll2[0] and roll2[1]>roll2[2]):
		mid2=roll2[1]


	if(roll2[2]>roll2[0] and roll2[2]>roll2[1]):
		high2=roll2[2]
	if(roll2[2]<roll2[0] and roll2[2]<roll2[1]):
		low2=roll2[2]
	if(roll2[2]>roll2[0] and roll2[2]<roll2[1]):
		mid2=roll2[2]
	if(roll2[2]<roll2[0] and roll2[2]>roll2[1]):
		mid2=roll2[2]

	if(roll2[1]>roll2[0] and roll2[1]> roll2[2]):
		high2=roll2[1]
	if(roll2[1]<roll2[0] and roll2[1]<roll2[2]):
		low2=roll2[1]
	if(roll2[1]>roll2[0] and roll2[1]<roll2[2]):
		mid2=roll2[1]
	if(roll2[1]<roll2[0] and roll2[1]>roll2[2]):
		mid2=roll2[1]

	if(roll2[1]==roll2[0] and roll2[0]>roll2[2]):
		high2=roll2[1]
		mid2=roll2[0]
	if(roll2[1] == roll2[0] and roll2[0]<roll2[2]):
		low2=roll2[0]
		mid2=roll2[1]

	if(roll2[1]==roll2[2] and roll2[2]>roll2[0]):
		high2=roll2[1]
		mid2=roll2[2]
	if(roll2[1] == roll2[2] and roll2[2]<roll2[0]):
		low2=roll2[2]
		mid2=roll2[1]
	if(roll2[2]==roll2[0] and roll2[0]>roll2[1]):
		high2=roll2[2]
		mid2=roll2[0]
	if(roll2[2] == roll2[0] and roll2[2]<roll2[1]):
		low2=roll2[0]
		mid2=roll2[2]
	if(roll2[0]==roll2[1] and roll2[0]==roll2[2]):
		high2=roll2[0]
		mid2=roll2[1]
		low2=roll2[2]
	print("\n\nFor {}, the high number is {}, the middle number is {}, and the lowest number is {}.".format(player2,high2,mid2,low2))
	
	highorlow1=0
	highorlow2=0
	if(high1<high2):
		highorlow1+=1
	if(high1>high2):
		highorlow2+=1
	if(mid1>mid2):
		highorlow2+=1
	if(mid1<mid2):
		highorlow1+=1
	if(low1<low2):
		highorlow1+=1
	if(low1>low2):
		highorlow2+=1
	if(highorlow1>highorlow2):
		win1+=1
	if(highorlow1<highorlow2):
		win2+=1
	if(highorlow1==highorlow2):
		print("\nYou both tied this round so no points for either side.")
	print("\nScore is {} to {} ({} to {}).".format(win1,win2,player1,player2))
if(win1==3):
	print("\nCongrats! {} won the game!".format(player1))
else:
	print("\nCongrats! {} won the game!".format(player2))