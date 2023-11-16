from tkinter import Frame, Entry, Label
import game


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.text_label = Label(self)
        self.text_label.pack()

        self.entry = Entry(self)
        self.entry.pack()

        self.game = game.Game()
        self.game.start_game()
        self.text_label["text"] = self.game.untyped_text

        self.entry.bind('<KeyRelease>', self.check_typed_letter)
        print("Game started")

    def check_typed_letter(self, event):
        print(event.char)
        letter = event.char
        if self.game.letter_typed(letter):
            self.text_label["text"] = self.game.untyped_text
            self.entry.delete(0, 1)
            if not self.game.untyped_text:
                self.game.end_game()
                self.text_label["text"] = "WPM: " + str(self.game.get_wpm()) + " Accuracy: " + str(self.game.get_accuracy())
                self.entry.unbind('<KeyRelease>')
