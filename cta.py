import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import time
import threading
import configparser

class SoundMapper:
    def __init__(self):
        self.sound_map = {
            "Work": "sounds/break_sound.wav",
            "Break": "sounds/work_sound.wav"
        }

    def get_sound_file(self, key):
        return self.sound_map.get(key, None)
    
class PomodoroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("300x500")
        self.master.resizable(False, False)

        self.work_time = tk.IntVar(value=1)
        self.break_time = tk.IntVar(value=1)
        self.load_preferences()
        self.current_timer = "Work"
        self.time_remaining = 0
        self.running = False

        self.setup_gui()
        self.update_timer_display()

    def setup_gui(self):
        self.timer_label = tk.Label(self.master, text=self.current_timer, font=("Arial", 24))
        self.timer_label.pack(pady=10)

        self.time_label = tk.Label(self.master, text="", font=("Arial", 24))
        self.time_label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.work_time_label = tk.Label(self.master, text="Work time (min):")
        self.work_time_label.pack()
        self.work_time_entry = tk.Entry(self.master, textvariable=self.work_time)
        self.work_time_entry.pack()

        self.break_time_label = tk.Label(self.master, text="Break time (min):")
        self.break_time_label.pack()
        self.break_time_entry = tk.Entry(self.master, textvariable=self.break_time)
        self.break_time_entry.pack()

        self.about_button = tk.Button(self.master, text="About", command=self.show_about)
        self.about_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=20, pady=10)

    def start_timer(self):
        self.work_time.set(int(self.work_time_entry.get()))
        self.break_time.set(int(self.break_time_entry.get()))
        self.save_preferences()

        if not self.running:
            self.running = True
            self.start_button.config(text="Pause")
            self.time_remaining = self.work_time.get() * 60
            threading.Thread(target=self.run_timer).start()
        else:
            self.running = False
            self.start_button.config(text="Resume")

    def run_timer(self):
        while self.time_remaining > 0 and self.running:
            mins, secs = divmod(self.time_remaining, 60)
            self.time_label.config(text="{:02d}:{:02d}".format(mins, secs))
            self.master.update()
            time.sleep(1)
            self.time_remaining -= 1

        if self.running:
            self.play_sound()
            self.switch_timer()
            self.start_timer()

    def switch_timer(self):
        if self.current_timer == "Work":
            self.current_timer = "Break"
            self.timer_label.config(text="Break")
            self.time_remaining = self.break_time.get() * 60
        else:
            self.current_timer = "Work"
            self.timer_label.config(text="Work")
            self.time_remaining = self.work_time.get() * 60

    def update_timer_display(self):
        self.time_label.config(text="{:02d}:{:02d}".format(self.work_time.get(), 0))

    def play_sound(self):
        sound_mapper = SoundMapper()
        sound_file = sound_mapper.get_sound_file(self.current_timer)
        if sound_file:
            playsound(sound_file)
        else:
            print("Error: Sound file not found for", self.current_timer)

    def show_about(self):
        messagebox.showinfo("About", "Chrono Tomato Automato\nVersion 1.0\nDeveloped by Sarah Kelley and ChatGPT-4")
    
    def save_preferences(self):
        config = configparser.ConfigParser()
        config["PREFERENCES"] = {
            "work_time": self.work_time.get(),
            "break_time": self.break_time.get()
        }

        with open("chrono-tomato-automato-preferences.ini", "w") as configfile:
            config.write(configfile)

    def load_preferences(self):
        config = configparser.ConfigParser()
        config.read("chrono-tomato-automato-preferences.ini")

        if "PREFERENCES" in config:
            self.work_time.set(config.getint("PREFERENCES", "work_time", fallback=25))
            self.break_time.set(config.getint("PREFERENCES", "break_time", fallback=5))

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
