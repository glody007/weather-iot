# importing matplotlib module
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from data import environment

# plot function is created for 
# plotting the graphs of params in list in 
# tkinter window
def plot_polluants_history(frame, polluants, dpi=30):
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = dpi)

    # adding the subplot
    plot = fig.add_subplot(111)
    
    # # Plot for params in the list
    for polluant in polluants:
        plot.plot(environment.get_polluant_history(polluant['name']))
  
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
    
