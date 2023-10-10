# Author = Gabriel Bennett
# Last edited = October 12th, 2023
# This python program allow the user to click a button and output a random anime for the user to watch.

# Below is the importation of tkinter, and random 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

# Below is the creation of the mai window thta is used for this program. Also the designing of the window.
quiz_one_wallpaper = PhotoImage(file = 'quiz_one_wallpaper.png')
quiz_one_window = Toplevel()
quiz_one_window.title("Which anime should you watch???")
quiz_one_window.geometry("1280x720")
quiz_one_wallpaper_label = Label(quiz_one_window, image = quiz_one_wallpaper)
quiz_one_wallpaper_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Below is te designation of ttk buttons that are used in this program.
button = ttk.Button
close_button = ttk.Button

# Below is an array of different anime.
answers = [
    "Hunter X Hunter",
    "Naruto",
    "Dragon Ball Z",
    "Attack on Titan",
    "Demon Slayer",  
    "Avatar the Last Airbender",
    "The Seven Deadly Sins",
    "One Punch Man",
    "Swort Art Online",
    "Pokemon",
    "Yu-Gi-Oh",
    "One Piece",
    "Digimon",
    "Legend of Korra",
    "My Hero Academia",]

# Below is the designation of the answer using the random funciton to randomly choose an anime from the given array of choices.
answer = random.choice(answers)

# Below is the function that calls on the messagebox that is used to display the random answer.
def on_click():
    messagebox.showinfo("Your random anime!", answer)

# Below is the creation of the button that allows the user torun the on click function. 
button = Button(quiz_one_window, text = "Choose your anime", command = on_click) 
button.pack(side = TOP) 

# Below is the function that allows the user to close the window all together. IT is calle don by the close button.
def close_window():
    quiz_one_window.destroy()

# Below is the button the button that calls on the close window funciton.
close = close_button(quiz_one_window,
                         text = "Close",
                         command = close_window)
close.pack(side = BOTTOM)

quiz_one_window.mainloop() 
