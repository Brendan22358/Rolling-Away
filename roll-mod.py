from random import randint
player1=raw_input("Enter player 1's name: ")
player2=raw_input("Enter player 2's name: ")
win1=0
win2=0
print("We are going to play a game called Dice Duels, except with different rules. Hint, There will be an easter egg can you find it?")
while(win1!=3 and win2!=3):
	player1roll=raw_input("{} type roll to roll three dye.\n>".format(player1))
	if(player1roll!="roll"):
		player1roll=raw_input("{} type roll to roll three dye.\n>".format(player1))
	roll1=[randint(1,7),randint(1,7),randint(1,7)]
	player2roll=raw_input("{} type roll to roll three dye.\n>".format(player2))
	if(player2roll!="roll"):
		player2roll=raw_input("{} type roll to roll three dye.\n>".format(player2))
	roll2=[randint(1,7),randint(1,7),randint(1,7)]
	print("{} got {}.".format(player1,roll1))
	print("{} got {}.".format(player2,roll2))
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


	if(roll1[2]>roll1[0] and roll1[2]>roll1[1]):
		high1=roll1[2]
	if(roll1[2]<roll1[0] and roll1[2]<roll1[1]):
		low1=roll1[2]
	if(roll1[2]>roll1[0] and roll1[2]<roll1[1]):
		mid1=roll1[2]
	if(roll1[2]<roll1[0] and roll1[2]>roll1[1]):
		mid1=roll1[2]
	print(high1,mid1,low1)
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
	print(high2,mid2,low2)

	