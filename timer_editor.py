import tkinter as tk
from tkinter import filedialog, messagebox
from abc import ABC, abstractmethod

class TimerEditor(tk.Frame, ABC):
    def __init__(self, master, timer, timer_list, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.timer = timer
        self.timer_list = timer_list

        # Name label and entry
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_var = tk.StringVar(value=timer.name)
        self.name_entry = tk.Entry(self, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1)

        # Duration label and entry
        self.duration_label = tk.Label(self, text="Duration:")
        self.duration_label.grid(row=1, column=0)
        self.duration_var = tk.StringVar(value=timer.duration)
        self.duration_entry = tk.Entry(self, textvariable=self.duration_var)
        self.duration_entry.bind('<Return>', self.update_duration)
        self.duration_entry.grid(row=1, column=1)

        # Time Remaining label and entry
        self.time_remaining_label = tk.Label(self, text="Time Remaining:")
        self.time_remaining_label.grid(row=2, column=0)
        self.time_remaining_var = tk.StringVar(value=timer.time_remaining)
        self.time_remaining_entry = tk.Entry(self, textvariable=self.time_remaining_var)
        self.time_remaining_entry.grid(row=2, column=1)

        # Start Sound label and entry
        self.start_sound_label = tk.Label(self, text="Start Sound:")
        self.start_sound_label.grid(row=3, column=0)
        self.start_sound_var = tk.StringVar(value=timer.start_sound)
        self.start_sound_entry = tk.Entry(self, textvariable=self.start_sound_var)
        self.start_sound_entry.grid(row=3, column=1)
        self.start_sound_button = tk.Button(self, text="Browse", command=self.browse_start_sound)
        self.start_sound_button.grid(row=3, column=2)

        # End Sound label and entry
        self.end_sound_label = tk.Label(self, text="End Sound:")
        self.end_sound_label.grid(row=4, column=0)
        self.end_sound_var = tk.StringVar(value=timer.end_sound)
        self.end_sound_entry = tk.Entry(self, textvariable=self.end_sound_var)
        self.end_sound_entry.grid(row=4, column=1)
        self.end_sound_button = tk.Button(self, text="Browse", command=self.browse_end_sound)
        self.end_sound_button.grid(row=4, column=2)

        # Enabled checkbox
        self.enabled_var = tk.BooleanVar(value=timer.enabled)
        self.enabled_check = tk.Checkbutton(self, text="Enabled", variable=self.enabled_var)
        self.enabled_check.grid(row=5, column=1)

        # Auto Start Next checkbox
        self.auto_start_next_var = tk.BooleanVar(value=timer.auto_start_next)
        self.auto_start_next_check = tk.Checkbutton(self, text="Auto Start Next", variable=self.auto_start_next_var)
        self.auto_start_next_check.grid(row=6, column=1)

        # Delete button
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_timer)
        self.delete_button.grid(row=7, column=0)

        # Up button
        self.up_button = tk.Button(self, text="Up", command=self.move_timer_up)
        self.up_button.grid(row=7, column=1)

        # Down button
        self.down_button = tk.Button(self, text="Down", command=self.move_timer_down)
        self.down_button.grid(row=7, column=2)

    def browse_start_sound(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
        if file_path:
            self.start_sound_var.set(file_path)
            self.timer.start_sound = file_path

    def browse_end_sound(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
        if file_path:
            self.end_sound_var.set(file_path)
            self.timer.end_sound = file_path

    def update_duration(self, event):
        try:
            new_duration = self.duration_var.get()
            self.timer.duration = new_duration
        except ValueError:
            messagebox.showerror("Invalid Duration", "Invalid duration entered. Please enter a valid duration.")

    def delete_timer(self):
        response = messagebox.askyesno("Delete Timer", "Are you sure you want to delete this timer?")
        if response:
            self.timer_list.remove(self.timer)
            self.destroy()

    def move_timer_up(self):
        index = self.timer_list.index(self.timer)
        if index > 0:
            self.timer_list[index - 1], self.timer_list[index] = self.timer_list[index], self.timer_list[index - 1]
            self.master.reorder_timers()

    def move_timer_down(self):
        index = self.timer_list.index(self.timer)
        if index < len(self.timer_list) - 1:
            self.timer_list[index + 1], self.timer_list[index] = self.timer_list[index], self.timer_list[index + 1]
            self.master.reorder_timers()

    def update_time_remaining_label(self):
        self.time_remaining_var.set(self.timer.time_remaining)

    @abstractmethod
    def update(self, subject):
        pass


class MyTimerEditor(TimerEditor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, subject):
        self.name_var.set(subject.name)
        self.duration_var.set(subject.duration)
        self.start_sound_var.set(subject.start_sound)
        self.end_sound_var.set(subject.end_sound)
        self.enabled_var.set(subject.enabled)
        self.auto_start_next_var.set(subject.auto_start_next)

