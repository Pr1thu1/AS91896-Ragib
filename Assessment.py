# Importing Tkinter and using PIL
import tkinter as tk
from PIL import Image, ImageTk

# Defining the size of the image
root = tk.Tk()
root.geometry("1920x1080")

# Opening the image
image = Image.open("background2.png")
# --- ADDED THE RESIZE LINE BELOW ---
image = image.resize((1920, 1080), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(image)

# Making the image the background image
bg_label = tk.Label(root, image=bg_image)

# Using .place to cover the entire screen
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_image

# Entry box
name_entry = tk.Entry(root, font=("Arial", 20), justify="center")

# Puts in the middle of the screen
name_entry.place(relx=0.5, rely=0.45, anchor="center")

# Continue button
continue_btn = tk.Button(root, text="Continue", font=("Arial", 15), width=15)
continue_btn.place(relx=0.5, rely=0.52, anchor="center")

root.mainloop()
