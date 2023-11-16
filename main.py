from tkinter import Tk
import ui


def main():
    root = Tk()
    app = ui.Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
