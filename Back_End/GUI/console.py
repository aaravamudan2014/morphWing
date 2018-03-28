from Tkinter import *   
from PIL import Image, ImageTk
import time
from numpy import arange, sin, pi
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use("Agg")
global root
photo = None
root = Tk()
root.title("MorphWing Backend")
root.geometry("1000x800")
root.configure(background='blue')
fig = plt.Figure()
x = np.arrange(0,2*np.pi, 0.01)
panel = Label(root)
f1 = Frame(root)
f2 = Frame(root)

def showMatPlot():
	fig = plt.Figure()
	canvas = FigureCanvasTkAgg(fig, master=root)
	canvas.get_tk_widget().grid(column=0,row=1)

	ax = fig.add_subplot(111)
	line, = ax.plot(x, np.sin(x))
	ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,


def startScreen():
	photo = ImageTk.PhotoImage(Image.open("/home/pi/Downloads/morph_wing_logo.jpg").resize((800,800)), Image.ANTIALIAS)
	panel.configure(image = photo)
	panel.image = photo;
	panel.pack(side = "left", fill = "both", expand = "yes")
def fullScreen():
	showMatPlot()
root.after(1000,startScreen)
root.after(2500, fullScreen)
time.sleep(2)
root.mainloop()


