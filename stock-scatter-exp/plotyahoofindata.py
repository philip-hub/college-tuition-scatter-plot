#imports everything need these packages will need to be installed using pip or pycharm.
import csv
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import tkinter as tk
from tkinter import filedialog
from scipy.optimize import curve_fit

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400, bg='lemon chiffon', relief='raised') #creates the tkinker window
canvas1.pack()


def func_exp(x, a, b, c):
    c = 16
    return a * (b ** x) + c

def caculate():
    FilePath = filedialog.askopenfilename()
    x = []
    y = []
    x3 = []
    N=1000
    filename = FilePath
    print(filename)
    with open(filename, 'r') as data:
        for line in csv.reader(data):
            #coverts csv data into a python list
            x.append(str(line[0]))
            y.append(line[5])
            print(x)
    #change the lists from text to int
    for i in range(0, len(x)):
        x2 = x[i]
        x2 = x2.split("/", 2)
        print(x2)
        months = x2[0]
        months = int(months)
        months = months * 30
        print(months)
        days = x2[1]
        days = int(days)
        years = x2[2]
        years = int(years)
        years = years*365
        print(years)
        days = days + months + years
        print(days)
        x[i] = float(days)

        """xSize = len(x)
        if i+1 == xSize:
            x[i+1] = float(days)
        elif i == xSize:
            x[i-1] = float(days)
        else:
            x[i-1] = float(days)"""




    for i in range(0, len(y)):
        y[i] = float(y[i])
        """ySize = len(y)
        if i+1 == ySize:
            y[i]=float(y[i])
        elif i == ySize:
            y[i] = float(y[i])
        else:
            y[i-1]=float(y[i])"""


    print(x)#prints the years to the terminal
    print(y)#prints the cost to the terminal

    colors = (1,0,0)
    area = np.pi*3

    # Plot's the data
    plt.title("Your Favorite College's Tuition")
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))  #Calculates the line of best fit
    plt.title('XBI')
    plt.xlabel('days since 2000')
    plt.ylabel('closing price adjusted')
    print(np.unique(x))#prints the years in the best fit line
    print(np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))#prints the cost in the best fit line



    x_data = np.array(x)
    y_data = np.array(y)

    popt, pcov = curve_fit(func_exp, x_data, y_data, p0=(1500, 0.01, 7500))
    print(popt)

    plt.plot(x_data, func_exp(x_data, *popt), color='xkcd:teal')

    plt.show()

browseButton_CSV  =  tk.Button(text=" Import CSV File", command=caculate, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))    #creates the button in the window and runs calculate()
canvas1.create_window(200, 150, window=browseButton_CSV)

root.mainloop()
