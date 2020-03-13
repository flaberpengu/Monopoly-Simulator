import matplotlib.pyplot as plt
import tkinter as tk

file = open("data.txt","r")
data = file.readlines()
file.close()

for i in range(len(data)):
    data[i] = data[i].split(';')
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

global xvals
global yvals
xvals = []
yvals = []

for j in range(len(data)):
    xvals.append(data[j][0])
    yvals.append(data[j][1])

global plotted
plotted = []

def basicPlot():
    global plotted
    plotted = plt.plot(xvals, yvals)
    plt.show()

def plotLines():
    plt.close()
    plt.plot(xvals, yvals)
    plt.show()
    #plt.hide()
    #plt.setp(plotted, 'b-')
    #plt.show()

def plotPoints():
    plt.close()
    plt.plot(xvals, yvals, 'r.')
    plt.show()
    #plt.hide()
    #plt.setp(plotted, 'r.')
    #plt.show()

#plotPoints()
#plotLines()

master = tk.Tk()
s = tk.Button(master, text="Start plot", command=basicPlot)
s.pack()
b = tk.Button(master, text="Red points", command=plotPoints)
b.pack()
#mainloop()
