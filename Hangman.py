#Hangman
import tkinter

def GUI():
    global blanks
    Game = tkinter.Tk()
    blank = tkinter.Label(text=blanks)
    prompt = tkinter.Label(text="What letter would you like to pick?")
    guess = tkinter.Entry()
    submit = tkinter.Button(text="Submit")
    blank.pack()
    prompt.pack()
    guess.pack()
    submit.pack()
    Game.mainloop()



test = "Hello World"
strikes = 0
blanks = []
for i in test:
    if i == " ":
        blanks.append(" ")
    else:
        blanks.append("_")

print(blanks)
GUI()
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