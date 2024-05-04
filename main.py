from tkinter import *
import settings
import utils

root = Tk()

#set color
root.configure(bg="gray")
#size:
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

root.title("Minesweeper Game")

#stop resizing
root.resizable(False,False)


#add an frame element
top_frame = Frame(root, bg='pink', width= 1440, height=utils.height_prct(25))
#where to place it
top_frame.place(x=0,y=0)

left_frame = Frame (root, bg="blue", width=utils.width_prct(25), height=utils.height_prct(75))
left_frame.place(x=0,y=180)

center_frame = Frame(root, bg="GREEN", width=utils.width_prct(75),height=utils.height_prct(75) )
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(75))

#Run the window
root.mainloop()