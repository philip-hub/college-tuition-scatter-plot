#imports everything need these packages will need to be installed using pip or pycharm.
import csv
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400, bg='lemon chiffon', relief='raised') #creates the tkinker window
canvas1.pack()

def caculate():
    FilePath = filedialog.askopenfilename()
    x = []
    y = []
    N=1000
    filename = FilePath
    print(filename)
    with open(filename, 'r') as data:
        for line in csv.reader(data):
            #coverts csv data into a python list
            x.append(line[0])
            y.append(line[1])
    #change the lists from text to int
    for i in range(0, len(x)):
        x[i] = int(x[i])
    for i in range(0, len(y)):
        y[i] = int(y[i])

    print(x)#prints the years to the terminal
    print(y)#prints the cost to the terminal

    colors = (1,0,0)
    area = np.pi*3

    # Plot's the data
    plt.title("Your Favorite College's Tuition")
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))  #Calculates the line of best fit
    plt.title('College Cost')
    plt.xlabel('years')
    plt.ylabel('cost')
    print(np.unique(x))#prints the years in the best fit line
    print(np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))#prints the cost in the best fit line
    plt.show()

browseButton_CSV  =  tk.Button(text=" Import CSV File", command=caculate, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))    #creates the button in the window and runs calculate()
canvas1.create_window(200, 150, window=browseButton_CSV)

root.mainloop()
