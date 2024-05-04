from tkinter import *
import settings

root = Tk()

#set color
root.configure(bg="gray")
#size:
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

root.title("Minesweeper Game")

#stop resizing
root.resizable(False,False)


#add an frame element
top_frame = Frame(root, bg='pink', width= 1440, height=180)
#where to place it
top_frame.place(x=0,y=0)
left_frame = Frame (root, bg="blue", width=360, height=540)
left_frame.place(x=0,y=180)

#Run the window
root.mainloop()