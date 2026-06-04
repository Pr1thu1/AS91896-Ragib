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
img = Image.open("../../Imgs/intro.png")
iw, ih = img.size
scale = max(w / iw, h / ih)
img = img.resize((int(iw * scale), int(ih * scale)), Image.BICUBIC)
img = img.crop(((img.width - w) // 2, (img.height - h) // 2,
                (img.width + w) // 2, (img.height + h) // 2))
bg = ImageTk.PhotoImage(img)
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg

# Picking a bubbly font based on OS
if platform.system() == "Darwin":
    font = "Chalkboard SE"
elif platform.system() == "Windows":
    font = "Comic Sans MS"
else:
    font = "DejaVu Sans"

# "Please Enter Your Name" label
tk.Label(root, text="Please Enter Your Name:", font=(font, 20, "bold"),
         fg="#1a5276", bg="#ffffff").place(relx=0.5, rely=0.76, anchor="center")

# Drawing rounded rectangles for the entry box and button
def rounded(canvas, w, h, r, color):
    for x1, y1, x2, y2, start in [(0, 0, r*2, r*2, 90), (w-r*2, 0, w, r*2, 0),
                                    (0, h-r*2, r*2, h, 180), (w-r*2, h-r*2, w, h, 270)]:
        canvas.create_arc(x1, y1, x2, y2, start=start, extent=90, fill=color, outline=color)
    canvas.create_rectangle(r, 0, w-r, h, fill=color, outline=color)
    canvas.create_rectangle(0, r, w, h-r, fill=color, outline=color)

# Name entry box
ec = tk.Canvas(root, width=400, height=58, bg="#ffffff", highlightthickness=0)
ec.place(relx=0.5, rely=0.83, anchor="center")
rounded(ec, 400, 58, 20, "#C8EDF7")

name_entry = tk.Entry(root, font=("Arial", 22), justify="center",
                      bg="#C8EDF7", fg="#1a5276", bd=0, highlightthickness=0)
name_entry.place(relx=0.5, rely=0.83, width=370, height=48, anchor="center")

# Play button with hover and click effects
bc = tk.Canvas(root, width=80, height=60, bg="#ffffff", highlightthickness=0, cursor="hand2")
bc.place(relx=0.5, rely=0.93, anchor="center")

def draw_btn(color):
    bc.delete("all")
    rounded(bc, 80, 60, 20, color)
    bc.create_text(40, 30, text="▶", font=("Arial", 26, "bold"), fill="white")

draw_btn("#C8EDF7")
bc.bind("<Enter>",    lambda e: draw_btn("#a8d8f0"))
bc.bind("<Leave>",    lambda e: draw_btn("#C8EDF7"))
bc.bind("<Button-1>", lambda e: [draw_btn("#7bbedd"), root.after(150, lambda: draw_btn("#a8d8f0"))])


bc = tk.Canvas(root, width=40, height=40, bg="#ffffff", highlightthickness=0, cursor="hand2")
bc.place(relx=0.05, rely=0.1, anchor="center")

def draw_btn(color):
    bc.delete("all")
    rounded(bc, 40, 40, 20, color)
    bc.create_text(20, 20, text="X", font=("Arial", 20, "bold"), fill="#166C99")

draw_btn("#C8EDF7")
bc.bind("<Enter>",    lambda e: draw_btn("#a8d8f0"))
bc.bind("<Leave>",    lambda e: draw_btn("#C8EDF7"))
bc.bind("<Button-1>", lambda e: [draw_btn("#7bbedd"), root.after(150, lambda: draw_btn("#a8d8f0"))])

# Exit the quiz button
bc = tk.Canvas(root, width=40, height=40, bg="#ffffff", highlightthickness=0, cursor="hand2")
bc.place(relx=0.05, rely=0.1, anchor="center")

def draw_btn(color):
    bc.delete("all")
    rounded(bc, 40, 40, 20, color)
    bc.create_text(20, 20, text="X", font=("Arial", 20, "bold"), fill="#166C99")

draw_btn("#C8EDF7")
bc.bind("<Enter>",    lambda e: draw_btn("#a8d8f0"))
bc.bind("<Leave>",    lambda e: draw_btn("#C8EDF7"))
bc.bind("<Button-1>", lambda e: [
    draw_btn("#7bbedd"),
    root.after(150, lambda: [draw_btn("#a8d8f0"), root.destroy()])
])

# Loop program
root.mainloop()
