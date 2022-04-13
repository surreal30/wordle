import getpass
import emoji
answer_word = getpass.getpass("Word of the day: ")
l1 = list(answer_word)
print("""Rules:
1. You have total 6 tries to guess the word correctly.
2. If the letter of the word is correct at the corresponsing place of the answer. It will print G at that place.
3. If the letter is wrong it will print B.
""")
for i in range(1, 6):
	try_word = input("Enter your try:  ")
	l2 = list(try_word)
	trial = []
	fg = 0
	for j in range(5):
		if(l1[j] == l2[j]):
			trial.append(emoji.emojize(':green_square:'))
			fg += 1
		else:
			trial.append(emoji.emojize(':brown_square:'))
	if(fg==5):
		print("Correct word! ", answer_word)
		break
	else:
		print("Oops! Something is not quite right! Try again ", trial)
if(fg!=5):
	print("Better luck next time. The word is: ", answer_word)