from tkinter import *
import settings
import utils
from cell import Cell
root = Tk()

#set color
root.configure(bg="gray")
#size:
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')

root.title("Minesweeper Game")

#stop resizing
root.resizable(False,False)


#add an frame element
top_frame = Frame(root, bg='pink',  width=settings.WIDTH,
    height=utils.height_prct(25))
#where to place it
top_frame.place(x=0,y=0)

left_frame = Frame (root, bg="blue", width=utils.width_prct(25), height=utils.height_prct(75))
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(root, bg="GREEN", width=utils.width_prct(75),height=utils.height_prct(75) )
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))


for X in range(settings.GRID_SIZE):
    for Y in range(settings.GRID_SIZE):
        c = Cell(x=X, y=Y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=X, row=Y)


#call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)
Cell.reandomize_mines()
#Run the window
root.mainloop()