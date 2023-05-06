import threading
import time
from playsound import playsound

class TimerLoop(threading.Thread):
    def __init__(self, timer_list, app_running):
        super().__init__()
        self.timer_list = timer_list
        self.stop_loop = False
        self.app_running = app_running

    def run(self):
        while self.app_running.get():
            print("loop...")
            for timer in self.timer_list:
                if timer.enabled and timer.running:
                    timer.update_time_remaining()

                    if timer.time_remaining == "0:00":
                        playsound(timer.end_sound, block=False)
                        timer.stop()

                        if timer.start_next:
                            next_index = (self.timer_list.index(timer) + 1) % len(self.timer_list)
                            next_timer = self.timer_list[next_index]
                            if next_timer.enabled:
                                next_timer.start()

            time.sleep(1)

    def stop(self):
        self.stop_loop = True
