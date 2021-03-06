# WORDLE IMPLEMENTED IN PYTHON

import getpass
import emoji

answer_word = getpass.getpass("Word of the day: ")
word_length = len(list(answer_word))
l1 = list(answer_word)

print("""Rules:
1. You have total 6 tries to guess the word correctly.
2. If the letter of the word is correct at the corresponsing place of the answer. It will print """, emoji.emojize(':green_square:'), """ at that place.
3. If the letter is wrong it will print """, emoji.emojize(':brown_square:'), """.
""")

print("The word is of length ", word_length, ". All the best!")

for i in range(1, word_length+1):
	try_word = input("Enter your try:  ")
	l2 = list(try_word)
	trial = []
	fg = 0
	for j in range(word_length):
		if(l1[j] == l2[j]):
			trial.append(emoji.emojize(':green_square:'))
			fg += 1
		else:
			trial.append(emoji.emojize(':brown_square:'))
	if(fg==word_length):
		print("Correct word! ", ' '.join(map(str, trial)))
		print(answer_word)
		break
	else:
		print("Oops! Something is not quite right! Try again ", ' '.join(map(str, trial)))

if(fg!=word_length):
	print("Better luck next time. The word is: ", answer_word)
