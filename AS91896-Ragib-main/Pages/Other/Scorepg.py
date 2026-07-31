# Importing Tkinter and PIL
import tkinter as tk
import platform
from PIL import Image, ImageTk

# Setting up the window
root = tk.Tk()
root.lift()
root.attributes('-topmost', True)
root.after(100, lambda: root.attributes('-topmost', False))
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

# Getting screen size
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# Loading and fitting the background image
img = Image.open("../../Imgs/score.png")
iw, ih = img.size
scale = max(w / iw, h / ih)
img = img.resize((int(iw * scale), int(ih * scale)), Image.BICUBIC)
img = img.crop(((img.width - w) // 2, (img.height - h) // 2,
                (img.width + w) // 2, (img.height + h) // 2))
bg = ImageTk.PhotoImage(img)
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg

blue = "#1a6fa0"
blue_dark = "#155d87"
blue_click = "#0f4566"

# Read the final score from file
with open("../../score.txt", "r") as f:
    final_score = f.read().strip()

# Show the score on screen
tk.Label(root, text=final_score + " / 15", font=("Arial", 60, "bold"),
         fg="#1a5276", bg="#ffffff").place(relx=0.5, rely=0.60, anchor="center")



# Loop program
root.mainloop()
