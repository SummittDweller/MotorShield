#!/usr/bin/python

# GUI Code for PiMotor Shield V2
# Developed by: Mark McFate

import tkinter as tkinter
import PiMotor
import time

m1 = PiMotor.Motor("MOTOR1", 1)

aclose = PiMotor.Arrow(2)
aopen = PiMotor.Arrow(4)

limit = 5    # movement limit in seconds

def Start(check):
  print(check)
  print("check")


def M1Start():
  speed = float(w1.get())
  motor_button[0].configure(bg='green', activebackground="gray")
  motor_button[1].configure(bg='white', activebackground="red")
  print("Motor1 control opened")
  print("-->Speed @ %s" % speed)
  s = 0
  if var1.get() == 1:
    print("Opening...")
    aopen.on()
    while (s < limit):
      m1.reverse((speed))
      time.sleep(1)
      s += 1
    print("Time limit exceeded! Stopping.")
    aopen.off()
    m1.stop()
  elif var1.get() == 2:
    print("Closing...")
    aclose.on()
    while (s < limit):
      m1.forward((speed))
      time.sleep(1)
      s += 1
    print("Time limit exceeded! Stopping.")
    aclose.off()
    m1.stop()
  else:
    print("M1 - Error")
    aopen.off()
    aclose.off()
    m1.stop()

def M1Stop():
  print("Stopped!")
  aopen.off()
  aclose.off()
  m1.stop()




window = tkinter.Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth() / 3 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 4 - windowHeight / 2)

# Position the window
window.geometry("680x600+{}+{}".format(positionRight, positionDown))

window.title("Casement Window Control - GUI")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack(fill='both', expand='1')
frame.configure(bg='black')


#  Motor Start/Stop Button
BUTTON = [(50, 205), (153, 205), (50, 525), (153, 525),
          (470, 205), (573, 205), (470, 525), (573, 525)]
FUNC = [("START", "white", "green", M1Start), ("STOP", "red", "gray", M1Stop) ]

motor_button = []
for b in range(2):
    cmd = lambda x=b: FUNC[b][2]
    m_button = tkinter.Button(frame, height=1, width=4, text=FUNC[b][0],
                              fg="black", bg=FUNC[b][1], command=FUNC[b][3],
                              highlightthickness=0,
                              activebackground=FUNC[b][2])
    m_button.place(x=BUTTON[b][0], y=BUTTON[b][1])
    motor_button.append(m_button)

#  Labels
LABELS = [(" Left Casement Window ", 15, "OliveDrab1", 40, 70),
          (" GUI Casement Window Control ", 30, "White", 50, 5),
          (" Direction: ", 12, "SkyBlue1", 40, 95),
          (" % Speed: ", 12, "SkyBlue1", 50, 160)]

for b in range(4):
    lbl = tkinter.Label(frame, text=LABELS[b][0], bg="#000000", # bg="#383a39",
                        font=('times', LABELS[b][1], 'bold'), fg=LABELS[b][2])
    lbl.place(x=LABELS[b][3], y=LABELS[b][4])



#  Motor Direction Radio Buttons
var1 = tkinter.IntVar()
var1.set(1)
tkinter.Radiobutton(frame, highlightthickness=0, text="Open ", variable=var1,
                    value=1).place(x=41, y=125)
tkinter.Radiobutton(frame, highlightthickness=0, text="Close ",
                    variable=var1, value=2).place(x=127, y=125)
w1 = tkinter.Spinbox(width=5, values=(100, 90, 80, 70, 60, 50, 40, 30, 20, 10))
w1.place(x=145, y=160)

