# importing matplotlib module
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
 

# plot function is created for 
# plotting the graph in 
# tkinter window


def plot_temperature_history(frame):
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 40)

    # adding the subplot
    plot = fig.add_subplot(111)
    
    # x-axis values
    x = [5, 2, 9, 4, 7]
    
    # Y-axis values
    y = [10, 5, 8, 4, 2]
    
    # # Function to plot
    plot.bar(x,y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = frame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    
def plot_humidity_history(frame):
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 40)

    # adding the subplot
    plot = fig.add_subplot(111)
    
    # x-axis values
    x = [5, 2, 9, 4, 7]
    
    # Y-axis values
    y = [5, 5, 2, 5, 1]
    
    # # Function to plot
    plot.bar(x,y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = frame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    
def plot_pm10_history(frame):
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 40)

    # adding the subplot
    plot = fig.add_subplot(111)
    
    # x-axis values
    x = [5, 2, 9, 4, 7]
    
    # Y-axis values
    y = [1, 6, 6, 1, 2]
    
    # # Function to plot
    plot.bar(x,y)
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = frame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   frame)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()