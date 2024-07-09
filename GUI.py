import tkinter as tk
import mouse
import time

class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("400x300+500+200")
        self.win.title("My application")
        self.win.resizable(False, False)

        self.isClicking = False

        self.update()
        self.win.mainloop()

        self.auto_clicker()

    def set_clicker(self):
        if self.isClicking:
            self.isClicking = False
            print("Кликер отключен")
        else:
            self.isClicking = True
            print("Кликер включен")

    def auto_clicker(self):
        while True:
            if self.isClicking:
                mouse.double_click(button = "left")
                time.sleep(0.01)
    
    def createButtons(self):
        startButton = tk.Button(self.win, text="Start", font=("Arial 16 bold", 18), command=self.set_clicker)
        startButton.place(relx=0.6, rely=0.2, anchor=tk.CENTER)

    def update(self):
        self.createButtons()
