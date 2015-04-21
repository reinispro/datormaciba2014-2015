import Tkinter as tk

def update_timeText():
    if (state):
        global timer
        timer[2] += 1
        
        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1
        
        if (timer[1] >= 60):
            timer[0] += 1
            timer[1] = 0
        
        timeString = pattern.format(timer[0], timer[1], timer[2])
        
        timeText.configure(text=timeString)
        
    root.after(10, update_timeText)


def start():
    global state
    state = True


def pause():
    global state
    state = False

def reset():
    global timer
    timer = [0, 0, 0]
    timeText.configure(text='00:00:00')

def exist():
    root.destroy()

state = False

root = tk.Tk()
root.wm_title('Simple Kitchen Timer Example')

timer = [0, 0, 0]

pattern = '{0:02d}:{1:02d}:{2:02d}'

timeText = tk.Label(root, text="00:00:00", font=("Helvetica", 150))
timeText.pack()

startButton = tk.Button(root, text='Sakt', command=start)
startButton.pack()

pauseButton = tk.Button(root, text='Apturet', command=pause)
pauseButton.pack()

resetButton = tk.Button(root, text='Nodzest', command=reset)
resetButton.pack()

quitButton = tk.Button(root, text='Aizvert', command=exist)
quitButton.pack()

update_timeText()
root.mainloop()
