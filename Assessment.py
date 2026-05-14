# Imported tkinter and PIL
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# Sizing to fit different screens
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")

# Background image
image = Image.open("background2.png")
image = image.resize((width, height), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_image

# Asking user to enter their name
title_label = tk.Label(root, text="Please Enter Your Name:", font=("Arial", 20, "bold"),
                       fg="#1a5276", bg="#ffffff")
title_label.place(relx=0.5, rely=0.76, anchor="center")

# Name Entry Box
name_entry = tk.Entry(root, font=("Arial", 24), justify="center",
                      bg="#C8EDF7", fg="black", bd=0, relief="sunken",
                      highlightbackground="#ffffff", highlightthickness=2)
name_entry.place(relx=0.5, rely=0.83, width=400, height=50, anchor="center")

# Continue button
continue_btn = tk.Label(
    root,
    text="▶",
    font=("Arial", 45, "bold"),
    width=2,
    bg="#c8edf7",
    fg="white",
    cursor="hand2",
    bd=0,
    relief="flat"
)

continue_btn.place(relx=0.5, rely=0.93, anchor="center")

# Loop program
root.mainloop()
