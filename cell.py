from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object = None

    def create_btn_object(self,location):
        btn = Button(location, text="text")

        btn.bind('<Button-1>',self.left_click_actions) ## by convention <Button-1> means left click in Tinker!
        btn.bind('<Button-3>',self.right_click_actions) ## by convention <Button-3> means right click in Tinker!
        self.cell_btn_object = btn

    def left_click_actions(self,event):
        print(event)
        print("Left Clicked!")

    def right_click_actions(self,event):
        print(event)
        print("right Clicked!")