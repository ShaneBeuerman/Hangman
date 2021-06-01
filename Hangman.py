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
        if "_" not in blanks:
            winPopup()
    else:
        strikes += 1
        print("You have", strikes, "strikes")
        drawGallows()

def text_based_hangman():
    global strikes
    global test
    global blanks
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

def drawGallows():
    global gallows
    global strikes
    if strikes == 1:
        gallows.create_oval(40,40,60,60)
        #30, 40, 70, 60
    if strikes == 2:
        print("Body")
        gallows.create_line(50, 60, 50, 80)
    if strikes == 3:
        print("Left Arm")
        gallows.create_line(50, 70, 40, 60)
        #Left Arm
    if strikes == 4:
        print("Right Arm")
        gallows.create_line(60, 60, 50, 70)
        #Right Arm
    if strikes == 5:
        print("Left Leg")
        gallows.create_line(50, 80, 40, 90)
        #Left Leg
    if strikes == 6:
        print("Right Leg")
        #Right Leg
        gallows.create_line(50, 80, 60, 90)
        losePopup()

def winPopup():
    win = tkinter.Tk()
    win.wm_title("You win.")
    winLabel = tkinter.Label(win, text="You have won!")
    winButton = tkinter.Button(win, text="Okay", command = win.destroy)
    winLabel.pack()
    winButton.pack()
    win.mainloop()

def losePopup():
    lose = tkinter.Tk()
    lose.wm_title("You lose.")
    loseLabel = tkinter.Label(lose, text="You have lost!")
    loseButton = tkinter.Button(lose, text="Okay", command = lose.destroy)
    loseLabel.pack()
    loseButton.pack()
    lose.mainloop()
        
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
gallows.create_line(0, 100, 100, 100)
gallows.create_line(25, 100, 25, 25)
gallows.create_line(25, 25, 50, 25)
gallows.create_line(50, 25, 50, 40)
blank.pack()
prompt.pack()
guess.pack()
submit.pack()
gallows.pack()
Game.mainloop()
