# main.py
import tkinter as tk
from tkinterdnd2 import TkinterDnD
from app_ui import PhotoToPdfApp


def main():
    root = TkinterDnD.Tk()
    app = PhotoToPdfApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
