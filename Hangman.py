#Hangman
import tkinter 

#Udates the GUI after a new letter has been submitted. 
def updateGUI(letter):
    global blanks
    global blank
    global puzzle
    global strikes
    if letter.lower() in puzzle:
        for i in range(len(puzzle)):
            if puzzle[i] == letter.lower():
                blanks[i] = letter.lower()
        blank.config(text=blanks)
        if "_" not in blanks:
            winPopup()
    else:
        strikes += 1
        drawGallows()

#A text-based version of hangman that was used before
#the GUI was built.
def text_based_hangman():
    global strikes
    global puzzle
    global blanks
    while strikes < 5 and "_" in blanks:
        letter = input("What letter would you like to pick?")
        if letter not in puzzle:
            strikes += 1
            print("You have", strikes)
        else:
            for i in range(len(puzzle)):
                if puzzle[i] == letter:
                    blanks[i] = letter
    if strikes < 5:
        print("You win")
    else:
        print("You lose")

#Draws a shape based on how many strikes you have. If you have
#six strikes, a popup shows up alerting you that you have lost.
def drawGallows():
    global gallows
    global strikes
    if strikes == 1:
        gallows.create_oval(40,40,60,60)
        #Head
    if strikes == 2:
        gallows.create_line(50, 60, 50, 80)
        #Body
    if strikes == 3:
        gallows.create_line(50, 70, 40, 60)
        #Left Arm
    if strikes == 4:
        gallows.create_line(60, 60, 50, 70)
        #Right Arm
    if strikes == 5:
        gallows.create_line(50, 80, 40, 90)
        #Left Leg
    if strikes == 6:
        #Right Leg
        gallows.create_line(50, 80, 60, 90)
        losePopup()

#Pop up that shows up when you win. Click the button to move on.
def winPopup():
    win = tkinter.Tk()
    win.wm_title("You win.")
    winLabel = tkinter.Label(win, text="You have won!")
    winButton = tkinter.Button(win, text="Okay", command = win.destroy)
    winLabel.pack()
    winButton.pack()
    win.mainloop()

#Pop up that shows up when you lose. Click the button to move on.
def losePopup():
    lose = tkinter.Tk()
    lose.wm_title("You lose.")
    loseLabel = tkinter.Label(lose, text="You have lost!")
    loseButton = tkinter.Button(lose, text="Okay", command = lose.destroy)
    loseLabel.pack()
    loseButton.pack()
    lose.mainloop()

#Pop up that shows up when you input more than one character. Click the button
#to move on.
def errorPopup():
    error = tkinter.Tk()
    error.wm_title("Error")
    errorLabel = tkinter.Label(error, text="Sorry, just one character please.")
    errorButton = tkinter.Button(error, text="Okay", command = error.destroy)
    errorLabel.pack()
    errorButton.pack()
    error.mainloop()

#Submits the string that was in the entry field. If it is longer than one
#letter long, it is rejected and an error popup shows up.
def submit():
    global guess   
    letter = str(guess.get())
    if len(letter) > 1:
        errorPopup()
        return
    updateGUI(letter)

#Submits the string that was in the puzzle_input and adds each letter to
#the puzzle string that is used for the hangman puzzle.
def inputHangman():
    global puzzle
    global hangman
    global Prompt
    puzzle_input = str(hangman.get())
    for i in puzzle_input:
        puzzle += i.lower()
    Prompt.destroy()

puzzle = ""
#The prompt before the actual puzzle. Type out your hangman puzzle
#and press the button to submit it.
Prompt = tkinter.Tk()
label = tkinter.Label(text="Please type out your hangman Puzzle.")
hangman = tkinter.Entry()
submit1 = tkinter.Button(text="Confirm", command = inputHangman)
label.pack()
hangman.pack()
submit1.pack()
Prompt.mainloop() 

strikes = 0
blanks = []
for i in puzzle:
    if i == " ":
        blanks.append("")
    else:
        blanks.append("_")

#Builds the GUI that lets you see the puzzle, the gallows, allows
#you to type out a letter, and a button to submit that letter.
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
