import tkinter as tk
from tkinter import messagebox, ttk
import configparser
from timer import Timer
from timer_editor import TimerEditor, MyTimerEditor

class TimerGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_running = True
        self.title("Chrono Tomato Automato")
        self.timer_list = []

        # Top frame with buttons
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side=tk.TOP, pady=5)

        self.add_timer_button = tk.Button(self.top_frame, text="Add Timer", command=self.add_timer)
        self.add_timer_button.pack(side=tk.LEFT, padx=5)

        self.start_seq_button = tk.Button(self.top_frame, text="Start Seq", command=self.start_seq)
        self.start_seq_button.pack(side=tk.LEFT, padx=5)

        self.stop_seq_button = tk.Button(self.top_frame, text="Stop Seq", command=self.stop_seq)
        self.stop_seq_button.pack(side=tk.LEFT, padx=5)

        self.reset_all_button = tk.Button(self.top_frame, text="Reset All Timers", command=self.reset_all_timers)
        self.reset_all_button.pack(side=tk.LEFT, padx=5)

        # Scrollable pane with TimerEditor instances
        self.scrollable_frame = ttk.Frame(self)
        self.scrollable_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scrollable_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.scrollable_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)

        self.timers_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.timers_frame, anchor=tk.NW)

        self.load_preferences()
        
    def add_timer(self):
        if len(self.timer_list) < 9:
            new_timer = Timer()
            timer_editor = MyTimerEditor(self.timers_frame, timer=new_timer, timer_list=self.timer_list)
            timer_editor.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            self.timer_list.append(new_timer)

    def start_seq(self):
        for timer in self.timer_list:
            if timer.enabled and not timer.running:
                timer.start()
                break

    def stop_seq(self):
        for timer in self.timer_list:
            if timer.running:
                timer.stop()

    def reset_all_timers(self):
        for timer in self.timer_list:
            timer.stop()
            timer.reset()

    def reorder_timers(self):
        for widget in self.timers_frame.winfo_children():
            widget.pack_forget()
        for timer in self.timer_list:
            for widget in self.timers_frame.winfo_children():
                if widget.timer == timer:
                    widget.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                    break

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def load_preferences(self):
        config = configparser.ConfigParser()
        config.read('chrono-tomato-automato.ini')

        if 'Timers' in config:
            num_timers = int(config['Timers']['num_timers'])

            for i in range(1, num_timers + 1):
                timer_config = config[f'Timer{i}']
                new_timer = Timer(name=timer_config['name'],
                                  duration=timer_config['duration'],
                                  start_sound=timer_config['start_sound'],
                                  end_sound=timer_config['end_sound'],
                                  enabled=timer_config.getboolean('enabled'),
                                  auto_start_next=timer_config.getboolean('auto_start_next'))
                timer_editor = TimerEditor(self.timers_frame, timer=new_timer, timer_list=self.timer_list)
                timer_editor.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
                self.timer_list.append(new_timer)

    def save_preferences(self):
        config = configparser.ConfigParser()
        config['Timers'] = {'num_timers': str(len(self.timer_list))}

        for i, timer in enumerate(self.timer_list, start=1):
            config[f'Timer{i}'] = {'name': timer.name,
                                   'duration': timer.duration,
                                   'start_sound': timer.start_sound,
                                   'end_sound': timer.end_sound,
                                   'enabled': str(timer.enabled),
                                   'auto_start_next': str(timer.auto_start_next)}

        with open('chrono-tomato-automato.ini', 'w') as configfile:
            config.write(configfile)


