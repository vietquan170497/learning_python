from random import randint

player = input("Nguoi chon Dam, La, Keo: ")
computer = randint(0,2)

if computer == 0:
	computer = "Keo"
if computer == 1:
	computer = "Dam"
if computer == 2:
	computer = "La"

if computer == 0:
	computer == "Dam"
if computer == 1:
	computer == "La"

print("May chon: " + computer)

if player == computer:
	print("Draw")
else:
	if player == "Keo":
		if computer == "Dam":
			print("Lost")
		else:
			print("Win")

	elif player == "Dam":
		if computer == "Keo":
			print("Win")
		else:
			print("Lose")

	elif player == "La":
		if computer == "Dam":
			print("Win")
		else:
			print("Lose")

	else:
		print("Nhap sai!")
