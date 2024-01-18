# Import required modules
from tkinter import *
import random

# Create the main application window
root = Tk()
root.geometry("700x450")  # Set the size of the window
root.title("Roll Dice")   # Set the title of the window
root.configure(bg='red')   # Set the background color of the window

# Create a label to display the dice result
label = Label(root, text="", font=("times", 260))

# Function to roll the dice and update the label with random dice faces
def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']  # Unicode characters for dice faces
    dice_faces = f'{random.choice(dice)}{random.choice(dice)}'
    
    # Choose a random color for the dice faces
    dice_colors = random.choice(['green', 'blue', 'purple', 'orange', 'yellow', 'black'])
    
    # Set the label text with random dice faces and random colors
    label.configure(text=dice_faces, fg=dice_colors, bg='red')  
    
    label.pack()  # Pack the label to update the display

# Set an icon for the application window
image_icon = PhotoImage(file="dice.png")
root.iconphoto(False, image_icon)

# Create a button to trigger the roll function
button = Button(root, text="Let's roll...", width=50, height=2, font=10, bg="grey", bd=2, command=roll)
button.pack(padx=10, pady=10)  # Pack the button with padding

# Start the Tkinter event loop
root.mainloop()
