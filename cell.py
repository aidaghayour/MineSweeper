from tkinter import Button, Label
import random
import settings


class Cell:

    all = []
    cell_count_label_object = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine=is_mine
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
        lbl = Label(location,text=f"Cells left:{settings.CELL_COUNT}")
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
        print(self.cell_btn_object.configure(text=self.surrounded_cells_mines_length))


    def show_mine(self):
        # A logic to interrupt the game and display lost message
        self.cell_btn_object.configure(bg="red")


    def right_click_actions(self,event):
        print(event)
        print("right Clicked!")

    @staticmethod
    def reandomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"