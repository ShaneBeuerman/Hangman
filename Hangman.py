#Hangman
import tkinter

def updateGUI(letter):
    global blanks
    global blank
    global test
    global strikes
    if letter in test:
        for i in range(len(test)):
            if test[i] == letter:
                blanks[i] = letter
        blank.config(text=blanks)
    else:
        strikes += 1
        print("You have", strikes, "strikes")
        
def errorPopup():
    error = tkinter.Tk()
    error.wm_title("Error")
    errorLabel = tkinter.Label(error, text="Sorry, just one character please.")
    errorButton = tkinter.Button(error, text="Okay", command = error.destroy)
    errorLabel.pack()
    errorButton.pack()
    error.mainloop()

def submit():
    global guess   
    letter = str(guess.get())
    if len(letter) > 1:
        print("Sorry, just one character please")
        errorPopup()
        return
    updateGUI(letter)
    print(letter)
    
test = "Hello World"
strikes = 0
blanks = []
for i in test:
    if i == " ":
        blanks.append(" ")
    else:
        blanks.append("_")

print(blanks)
Game = tkinter.Tk()
blank = tkinter.Label(text=blanks)
prompt = tkinter.Label(text="What letter would you like to pick?")
guess = tkinter.Entry()
submit = tkinter.Button(text="Submit", command=submit)
gallows = tkinter.Canvas(Game, width=100, height=100)
blank.pack()
prompt.pack()
guess.pack()
submit.pack()
gallows.pack()
Game.mainloop()
while strikes < 5 and "_" in blanks:
    letter = input("What letter would you like to pick?")
    if letter == 'quit':
        break
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