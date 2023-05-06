from timer import Timer
from timer_editor import TimerEditor
from timer_gui import TimerGui
from timer_loop import TimerLoop

if __name__ == "__main__":
    app = TimerGui()
    timer_loop = TimerLoop(app.timer_list)
    timer_loop.start()

    #app.protocol("WM_DELETE_WINDOW", timer_loop.stop)
    app.protocol("WM_DELETE_WINDOW", lambda: [timer_loop.stop(), app.save_preferences()])

    app.mainloop()

