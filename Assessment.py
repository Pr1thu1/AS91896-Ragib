# Importing Tkinter and using PIL
import tkinter as tk
from PIL import Image, ImageTk

# Defining the size of the image
root = tk.Tk()
root.geometry("1208x280")

# Opening the image
image = Image.open("background.png")
bg_image = ImageTk.PhotoImage(image)

# Making the image the background image
bg_label = tk.Label(root, image=bg_image)

# Using .place to cover the entire screen
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_image

root.mainloop()
