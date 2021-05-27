#Hangman

def printBlanks():
    print("To be continued")

test = "Hello World"
strikes = 0
blanks = []
for i in test:
    if i == " ":
        blanks.append(" ")
    else:
        blanks.append("_")

print(blanks)
while strikes < 5 and "_" in blanks:
    letter = input("What letter would you like to pick?")
    if letter not in test:
        strikes += 1
        print("You have", strikes)
    else:
        for i in range(len(test)):
            if test[i] == letter:
                blanks[i] = letter
    print(blanks)

if strikes < 5:
    print("You win")
else:
    print("You lose")