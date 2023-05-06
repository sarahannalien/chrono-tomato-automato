import tkinter as tk
from timer import Timer

class TimerGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.timer_list = []
        self.init_gui()

    def init_gui(self):
        self.master.title("Timer GUI")

        # Create a label and entry field for each timer attribute
        tk.Label(self, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self, text="Duration").grid(row=1, column=0)
        self.duration_entry = tk.Entry(self)
        self.duration_entry.grid(row=1, column=1)

        tk.Label(self, text="Start Sound").grid(row=2, column=0)
        self.start_sound_entry = tk.Entry(self)
        self.start_sound_entry.grid(row=2, column=1)

        tk.Label(self, text="End Sound").grid(row=3, column=0)
        self.end_sound_entry = tk.Entry(self)
        self.end_sound_entry.grid(row=3, column=1)

        self.auto_start_next_var = tk.BooleanVar()
        self.auto_start_next_var.set(False)
        tk.Checkbutton(self, text="Auto Start Next", variable=self.auto_start_next_var).grid(row=4, column=1)

        # Create buttons for adding, editing, and deleting timers
        tk.Button(self, text="Add Timer", command=self.add_timer).grid(row=5, column=1)
        tk.Button(self, text="Edit Timer", command=self.edit_timer).grid(row=5, column=0)
        tk.Button(self, text="Delete Timer", command=self.delete_timer).grid(row=5, column=2)

        # Create a scrollable list of timers
        self.timer_listbox = tk.Listbox(self, height=10)
        self.timer_listbox.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        # Bind a double-click event to the listbox to edit timers
        self.timer_listbox.bind("<Double-Button-1>", lambda event: self.edit_timer())

        # Pack the frame and center the window on the screen
        self.pack()
        self.center_window()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = (screen_width - self.master.winfo_reqwidth()) // 2
        y = (screen_height - self.master.winfo_reqheight()) // 2

        # Set the window position and size
        self.master.geometry("+{}+{}".format(x, y))

    def add_timer(self):
        # Create a new Timer object with the values from the entry fields
        name = self.name_entry.get()
        duration = float(self.duration_entry.get())
        start_sound = self.start_sound_entry.get()
        end_sound = self.end_sound_entry.get()
        auto_start_next = self.auto_start_next_var.get()
        timer = Timer(name, duration, start_sound, end_sound, auto_start_next)

        # Add the timer to the list and the listbox
        self.timer_list.append(timer)
        self.timer_listbox.insert(tk.END, str(timer))

        # Clear the entry fields
        self.name_entry.delete(0
