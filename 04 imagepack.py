from tkinter import *
from PIL import Image, ImageTk


instance_root = Tk()
instance_root.geometry("900x800")

# tree_image = PhotoImage(file='tree.png')

# for jpg image------

fish_image = Image.open("fish.jpg")
fish_photo = ImageTk.PhotoImage(fish_image)
tree_lable = Label(image = fish_photo)
tree_lable.pack()

instance_root.mainloop()