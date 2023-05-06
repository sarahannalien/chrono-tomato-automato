import tkinter as tk
from tkinter import ttk

from Timer import Timer
from TimerEditor import TimerEditor

class TimerEditorApp(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.timer_editors = []
        self.create_button = ttk.Button(self, text="Create Timer", command=self.create_timer)
        self.create_button.pack(padx=10, pady=10)
        self.update_timer_list()

    def create_timer(self):
        timer = Timer("", 0, "", "", False)
        editor = TimerEditor(self, timer)
        self.timer_editors.append(editor)
        self.update_timer_list()

    def update_timer_list(self):
        for editor in self.timer_editors:
            editor.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Timer Editor")
    app = TimerEditorApp(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

