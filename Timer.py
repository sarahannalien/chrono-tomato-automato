class Timer:
    def __init__(self, name, duration, start_sound, end_sound, auto_start_next=False):
        self.name = name
        self.duration = duration
        self.start_sound = start_sound
        self.end_sound = end_sound
        self.auto_start_next = auto_start_next

    def __str__(self):
        return f"Timer(name={self.name}, duration={self.duration}, start_sound={self.start_sound}, end_sound={self.end_sound}, auto_start_next={self.auto_start_next})"

