from tkinter import Frame, Entry, Label
import game
from math import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # make the window resizeable by the user
        #self.master.resizable(True, True)
        # set minimum size of the window
        self.master.geometry("800x600")
        # set the color of the background
        self.master.configure(bg="white")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.untyped_text_label = Label(self)
        self.untyped_text_label.pack()

        self.typed_text_label = Label(self)
        self.typed_text_label.pack()

        self.game = game.Game()
        self.game.start_game()
        self.untyped_text_label["text"] = self.game.get_untyped_text()
        self.typed_text_label["text"] = self.game.get_typed_text()

        self.master.bind('<KeyRelease>', self.check_typed_letter)
        print("Game started")

    def check_typed_letter(self, event):
        print(self.game.get_typed_text(), self.game.get_untyped_text())
        print(event.char)
        letter = event.char
        if self.game.typed_letter_correct(letter):
            self.update_text()
            if not self.game.untyped_text:
                self.untyped_text_label["text"] = "WPM: " + str(floor(self.game.get_wpm())) + " Accuracy: " + str(floor(self.game.get_accuracy())) + "%" + " Miss clicks: " + str(self.game.get_miss_clicks())
                self.game.end_game()
                self.master.unbind('<KeyRelease>')

    def update_text(self):
        self.untyped_text_label["text"] = self.game.get_untyped_text()
        self.typed_text_label["text"] = self.game.get_typed_text()
