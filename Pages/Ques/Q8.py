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
img = Image.open("../../Imgs/ques8.png")
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

# Answers
answer1 = "Spekkoek"
answer2 = "Polao"
answer3 = "Basashi"
answer4 = "Stargazy Pie"


# Option 1
btn1 = tk.Label(root, text="  " + answer1, font=("Arial", 26), fg="white", bg=blue, width=14, height=2, anchor="w", cursor="hand2", bd=0, relief="flat")
btn1.place(relx=0.16, rely=0.67, anchor="center")
btn1.bind("<Enter>", lambda e: btn1.config(bg=blue_dark))
btn1.bind("<Leave>", lambda e: btn1.config(bg=blue))
btn1.bind("<Button-1>", lambda e: btn1.config(bg=blue_click))

# Option 2
btn2 = tk.Label(root, text="  " + answer2, font=("Arial", 26), fg="white", bg=blue, width=14, height=2, anchor="w", cursor="hand2", bd=0, relief="flat")
btn2.place(relx=0.41, rely=0.67, anchor="center")
btn2.bind("<Enter>", lambda e: btn2.config(bg=blue_dark))
btn2.bind("<Leave>", lambda e: btn2.config(bg=blue))
btn2.bind("<Button-1>", lambda e: btn2.config(bg=blue_click))

# Option 3
btn3 = tk.Label(root, text="  " + answer3, font=("Arial", 26), fg="white", bg=blue, width=14, height=2, anchor="w", cursor="hand2", bd=0, relief="flat")
btn3.place(relx=0.16, rely=0.82, anchor="center")
btn3.bind("<Enter>", lambda e: btn3.config(bg=blue_dark))
btn3.bind("<Leave>", lambda e: btn3.config(bg=blue))
btn3.bind("<Button-1>", lambda e: btn3.config(bg=blue_click))

# Option 4
btn4 = tk.Label(root, text="  " + answer4, font=("Arial", 26), fg="white", bg=blue, width=14, height=2, anchor="w", cursor="hand2", bd=0, relief="flat")
btn4.place(relx=0.41, rely=0.82, anchor="center")
btn4.bind("<Enter>", lambda e: btn4.config(bg=blue_dark))
btn4.bind("<Leave>", lambda e: btn4.config(bg=blue))
btn4.bind("<Button-1>", lambda e: btn4.config(bg=blue_click))

# Loop program
root.mainloop()