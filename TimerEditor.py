import tkinter as tk
from tkinter import ttk

class TimerEditor(ttk.Frame):
    def __init__(self, master=None, timer=None, **kwargs):
        super().__init__(master, **kwargs)
        self.timer = timer
        self.name_label = ttk.Label(self, text="Name:")
        self.name_entry = ttk.Entry(self)
        self.name_entry.insert(0, timer.name if timer else "")
        self.duration_label = ttk.Label(self, text="Duration:")
        self.duration_entry = ttk.Entry(self)
        self.duration_entry.insert(0, timer.duration if timer else "")
        self.start_sound_label = ttk.Label(self, text="Start Sound:")
        self.start_sound_entry = ttk.Entry(self)
        self.start_sound_entry.insert(0, timer.start_sound if timer else "")
        self.end_sound_label = ttk.Label(self, text="End Sound:")
        self.end_sound_entry = ttk.Entry(self)
        self.end_sound_entry.insert(0, timer.end_sound if timer else "")
        self.auto_start_next_var = tk.BooleanVar()
        self.auto_start_next_var.set(timer.auto_start_next if timer else False)
        self.auto_start_next_checkbutton = ttk.Checkbutton(self, text="Auto Start Next", variable=self.auto_start_next_var)
        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_timer)
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.duration_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        self.start_sound_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.start_sound_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")
        self.end_sound_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.end_sound_entry.grid(row=3, column=1, padx=5, pady=5, sticky="we")
        self.auto_start_next_checkbutton.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.delete_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    def delete_timer(self):
        self.destroy()
        self.master.timer_editors.remove(self)
        del self

    def get_timer(self):
        return Timer(
            name=self.name_entry.get(),
            duration=int(self.duration_entry.get()),
            start_sound=self.start_sound_entry.get(),
            end_sound=self.end_sound_entry.get(),
            auto_start_next=self.auto_start_next_var.get(),
        )
