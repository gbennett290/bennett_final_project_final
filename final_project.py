# Author = Gabriel Bennett
# Last edited = October 12th, 2023
# this is a GUI for the Anime N'cyclopedia website that let the user take an anime trivia quiz, or decide what anime they should watch next.

# Below is the importing of tkinter and anything else needed for the program.
from tkinter import *
from tkinter import ttk

# Below is the creation of the main window and designing it. Also the designation of the wallpapers.
main_window = Tk()
main_window.title("Anime N'Cyclopedia")
main_window.geometry("1280x720")
main_wallpaper = PhotoImage(file = 'main_wallpaper.png')
main_label = Label(main_window, image = main_wallpaper)
main_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
quiz_one_wallpaper = PhotoImage(file = 'quiz_one_wallpaper.png')
quiz_two_wallpaper = PhotoImage(file = 'quiz_two_wallpaper.png')

# Below is the main funciton of the program that runs immediately. 
def main():
    # Below is the process of creating ttk buttons.
    button_quiz1 = ttk.Button
    button_quiz2 = ttk.Button
    button_quiz3 = ttk.Button
    button_close = ttk.Button
    # Below is the button allogation for the first button. It calls on the quiz one function.
    quiz_1 = button_quiz1(main_window, 
        text = "What anime should I watch?", 
        command = quiz_one)
    quiz_1.pack(side = TOP)
    # Below is the button allogation for the second button. It calls on the quiz anime trivia function.
    quiz_2 = button_quiz2(main_window, 
        text = "Anime Trivia",
        command = quiz_anime_trivia)
    quiz_2.pack(side = TOP)
    # Below is the button allogation for the third button. It calls on the quiz three function.
    quiz_3 = button_quiz3(main_window,
        text = "Anime Trivia",
        command = quiz_three)
    quiz_3.pack(side = TOP)
    # Below is the button allogation for the fourth button. It closes the program.
    close = button_close(main_window,
                         text = "Close",
                         command = close_window)
    close.pack(side = BOTTOM)

# Below is the function that gets called by the fourth buton in the main function. It is what closes the program.
def close_window():
    main_window.destroy()

# Below is the function tht is called on by the first button. It imports the python code for the random anime generator.
def quiz_one():
    import first_quiz
    first_quiz

# Below is the function that gets called on by the second button. It opens up a toplevel window.
def quiz_anime_trivia():
    anime_trivia_window = Toplevel()
    anime_trivia_window.title("Anime Trivia")
    anime_trivia_window.geometry("1280x720")
    quiz_one_wallpaper_label = Label(anime_trivia_window, image = quiz_one_wallpaper)
    quiz_one_wallpaper_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    # Below is the creation of the button that ten calls on the start quiz fumction.
    start_quiz_button = ttk.Button
    start_trivia_quiz = start_quiz_button(anime_trivia_window, 
        text = "Begin", 
        command = start_quiz)
    start_trivia_quiz.pack()
    
# Below is the function that is activated by the third button 
def quiz_three():
    quiz_two_window = Toplevel()
    quiz_two_window.title("blah blah blah")
    quiz_two_window.geometry("1280x720")
    quiz_one_wallpaper_label = Label(quiz_two_window, image = quiz_two_wallpaper)
    quiz_one_wallpaper_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Below is the function that is called on by the quiz anime trivia function. It opens up the anime trivia quiz.
def start_quiz():
    import anime_trivia_quiz
    anime_trivia_quiz

# Below is the calling on the main function to get the program running. 
main()
main_window.mainloop()
