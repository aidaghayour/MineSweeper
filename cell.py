from tkinter import Button, Label
import random
import settings
import ctypes # warnings and such
import sys

class Cell:

    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine=is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self,location):
        btn = Button(location, width=12,height=4)

        btn.bind('<Button-1>',self.left_click_actions) ## by convention <Button-1> means left click in Tinker!
        btn.bind('<Button-3>',self.right_click_actions) ## by convention <Button-3> means right click in Tinker!
        self.cell_btn_object = btn

    # can not be a cell method because only for the usecase of the class
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(location,text=f"Cells left:{Cell.cell_count}", width=12, height=4, fg="Black", font=("",30))
        Cell.cell_count_label_object = lbl

    def left_click_actions(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
    

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        # List comprehension
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1 

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # replace text of cell count with the new count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left:{Cell.cell_count}")
            self.cell_btn_object.configure (bg="SystemButtonFace") # if a flagged (orange) cell is pressed, the bg color is set to nromal
            self.is_opened = True


    def show_mine(self):
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine!", "Game Over", 0)
        self.cell_btn_object.configure(bg="red")
        sys.exit()


    def right_click_actions(self,event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="Orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False
    @staticmethod
    def reandomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"