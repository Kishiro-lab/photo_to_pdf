# main.py
import tkinter as tk
from app_ui import PhotoToPdfApp


def main():
    root = tk.Tk()
    app = PhotoToPdfApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
