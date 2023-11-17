from tkinter import Frame, Entry, Label
import game
from math import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # make the window resizeable by the user
        self.master.resizable(True, True)
        # set minimum size of the window
        self.master.minsize(400, 200)
        # set the background color of the window
        self.master.configure(bg="black")
        # set the title of the window
        self.master.title("type faster!")
        # place the frame in the center of the screen
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.create_widgets()

    def create_widgets(self):
        self.untyped_text_label = Label(self)
        self.untyped_text_label.grid(row=0, column=1)

        self.typed_text_label = Label(self)
        self.typed_text_label.grid(row=0, column=0)

        self.game = game.Game()
        self.game.start_game()
        self.untyped_text_label["text"] = self.game.get_untyped_text()
        self.typed_text_label["text"] = self.game.get_typed_text()

        self.master.bind('<KeyRelease>', self.check_typed_letter)
        print("Game started")

    def check_typed_letter(self, event):
        character = event.char
        if character == "":
            print("not allowed key pressed" + character)
            return

        if not self.game.typed_letter_correct(character):
            # color the last letter red
            pass
        self.update_text()

        if not self.game.get_untyped_text():
            self.display_results()
            self.game.end_game()
            self.master.unbind('<KeyRelease>')


    def update_text(self):
        self.untyped_text_label["text"] = self.game.get_untyped_text()
        self.typed_text_label["text"] = self.game.get_typed_text()

    def display_results(self):
        # clear the typed text widget
        self.typed_text_label["text"] = ""
        self.untyped_text_label["text"] = "WPM: " + str(
            floor(self.game.get_wpm())) + " Accuracy: " + str(
            floor(self.game.get_accuracy())) + "%" + " Miss clicks: " + str(
            self.game.get_miss_clicks())
