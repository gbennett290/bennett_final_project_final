# Author = Gabriel Bennett
# Last edited = October 12th, 2023
# This program allows the user to tak a quiz of 7 anime questions and then recieve a score out of seven.

# Below is the importaion of tkinter.
from tkinter import *

# Below is the array of questions that are used within the quiz.
questions = ["How many Dragon Balls are there?" ,
             "In the anime 'Hunter X Hunter', which family is famous for being assassins?" ,
             "Who is known as the 'One Punch Man'?" ,
             "What type of food does Naruto Uzumaki love the most?" ,
             "What was Ash ketchum's second pokemon?" ,
             "What is the title of the first Pokémon movie?" ,
             "What is the associated animal of the Sin of Pride (Escanor)?"]

# Below is the array of answer options that are correspondilly used with the questions within the quiz.
options = [["3","7","10","99"],
           ["Zoldyck","Freeces","Uzumaki","Krueger"],
           ["Naruto","Saitama","Goku","Ash"],
           ["Pizza","Waffles","Ramen","Ice Cream"],
           ["Caterpie","Bulbasaur","Tauros","Pidgeotto"],
           ["Pokemon: The First Movie - Mewtwo Strikes Back","I Choose You!","Pokemon: A Journey Has Begun","Detective Pikachu"],
           ["Bear","Lion","Snake","Rhino"]]

# Below is the array with the correct answers to the quiz.
answers = [2 , 1 , 2 , 3 , 4 , 1 , 2]

# Below is the starting point of the score keeper. 
score = 0

# Below is the total number of questions within the quiz.
total_No_questions = 7

# Below is the current question number that the user is on. This ets adjusted in the next function later. 
question_No = 1

# Below is the function that allows the quiz to correctly move onto the next question without any issues.
def next():
    # Below is global calling on the earlier designated score and question number.
    global score, question_No
    # Below is the designator that collects the data that the user enters and then converts it into a selected option that allows for keeping score.
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    elif val4.get() == 1:
        selected_option = 4
    else:
        selected_option = - 1

    if(answers[question_No - 1] == selected_option):
        score += 1

    question_No += 1

    # Below is the stop limit for the questions. Once the question number reaches higher than the total number of questions it stops the program and exports the score.
    if question_No > total_No_questions:
        root.pack_forget()
        Score.place(relx = .75, rely = .45)
        Score.config(text = "Score: " + str(score) + "/7")
    # Below is the continuation of the function that if the question number is less than or equal to the total number of questions it clears the earlier placed values and enters the new question.
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        val4.set(0)
        question.config(text = questions[question_No - 1])
        option1.config(text = options[question_No - 1][0])
        option2.config(text = options[question_No - 1][1])
        option3.config(text = options[question_No - 1][2])
        option4.config(text = options[question_No - 1][3])
        
# Below is the funciton that makes sure no more than one value is entered per question.
def check(option):
    if(option == 1):
        val2.set(0)
        val3.set(0)
        val4.set(0)
    elif(option == 2):
        val1.set(0)
        val3.set(0)
        val4.set(0)
    elif(option == 3):
        val1.set(0)
        val2.set(0)
        val4.set(0)
    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)

# Below is the creation of the main toplevel window used in this code. Also the designing of it as well.
trivia_window = Toplevel()
trivia_window.title("Quiz Page")
trivia_window.geometry('600x200')
trivia_wallpaper = PhotoImage(file = 'trivia_wallpaper.png')
trivia_label = Label(trivia_window, image = trivia_wallpaper)
trivia_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Below is the the creation of a frame that allows for out score to be placed into the tkinter window.
root = Frame()
root.pack()

# Below is the label that is used to display the questions.
question = Label(trivia_window, width = 60, font = (20), text = questions[0])
question.pack()

# Below is the designation of the values used in the quiz.
val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()

# Below is the creation of the check boxes utilized in the quiz. 
option1 = Checkbutton(trivia_window, variable = val1, text = options[0][0], command = lambda: check(1))
option1.pack()
option2 = Checkbutton(trivia_window, variable = val2, text = options[0][1], command = lambda: check(2))
option2.pack()
option3 = Checkbutton(trivia_window, variable = val3, text = options[0][2], command = lambda: check(3))
option3.pack()
option4 = Checkbutton(trivia_window, variable = val4, text = options[0][3], command = lambda: check(4))
option4.pack()

# Below is the creation of the next button that allows for the user to continue on with the quiz and go to the next question.
next_b = Button(trivia_window, text = "Next Question", command = next)
next_b.pack()

# Below is the label that is our score placer.
Score = Label(trivia_window)
Score.place_forget()

trivia_window.mainloop()
