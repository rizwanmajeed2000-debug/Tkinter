from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    """Print the event associated to the key pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\n The button was clicked!")

buton = Button(text="Click me!")
button.pack()

window.bind("<Button-1>", handle_click)

window.mainloop()