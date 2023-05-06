class Timer:
    _instance_count = 0

    def __init__(self, name=None, duration="", time_remaining="", start_sound="", end_sound="", enabled=False, running=False, auto_start_next=False):
        Timer._instance_count += 1
        self.name = name or f"Timer{Timer._instance_count}"
        self.duration = duration
        self.time_remaining = time_remaining
        self.start_sound = start_sound
        self.end_sound = end_sound
        self.enabled = enabled
        self.running = running
        self.auto_start_next = auto_start_next

    def __str__(self):
        return self.name


