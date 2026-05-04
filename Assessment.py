import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("800x600")

# 1. Load the image using PIL
image = Image.open("background.jpg")  # Supports JPG, PNG, etc.
# 2. Convert to a format Tkinter understands
bg_image = ImageTk.PhotoImage(image)

# 3. Create a Label to hold the image
bg_label = tk.Label(root, image=bg_image)
# 4. Use .place to cover the entire window
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Keep a reference to prevent garbage collection
bg_label.image = bg_image

root.mainloop()


print ("WELCOME to FOODQUIZ")
print ("test your knowledge of various foods around the world.")
play = input("Would you like to continue? (Yes/No)")
if play.lower() == "yes":
    print("Intructions:")
    print("")