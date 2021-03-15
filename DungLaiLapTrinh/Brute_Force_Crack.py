from random import randint

system_pass = "quannv"

guess = ""

while (guess!=system_pass):
	guess = ""
	for letter in range(len(system_pass)):
		guess_letter = password[randint(0,25)]
		guess = str(guess_letter) + str(guess)

	print(guess)

print("Your password:" + guess_letter)