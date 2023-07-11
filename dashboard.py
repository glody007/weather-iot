# Import Module
import math
from tkinter import *
from data import moment, location, environment
from graph import plot_polluants_history

PRIMARY = "#3b82f6"
ACCENT = "#60a5fa"
SECONDARY = "#6ee7b7"
DESTRUCTIVE = "#fda4af" 
BACKGROUND = "#cbd5e1"
SLATE = "#334155"

PARAM_COLUMNS = 4
PARAM_GENERAL_ROWS = math.ceil(len(environment.generals) / PARAM_COLUMNS)
PARAM_POLLUANT_ROWS = math.ceil(len(environment.polluants) / PARAM_COLUMNS)

# create root window
root = Tk()

# root background
root.configure(background=BACKGROUND)

# root window title and dimension
root.title("WEATHER IOT")
# Set geometry(widthxheight)
root.maxsize(1305, 784)
# set resizable width false
root.resizable(False, True)

# ------------- TOP BAR -------------

#Create top bar
top_frame = Frame(root, height=60)
top_frame.grid_columnconfigure(4, weight=1)
top_frame.grid(row=0, column=0, columnspan=4, sticky=EW)

# Create frames and labels in top_bar
logo_frame = Frame(top_frame)
logo_frame.grid(row=0, column=1, sticky=W)

place_hour_frame = Frame(top_frame)
place_hour_frame.grid(row=0, column=2, columnspan=3, padx=4, pady=4, sticky="E")

main_title = Label(logo_frame, text="WEATHER IOT", font='Montserrat 25 bold', fg=PRIMARY)
main_title.grid(row=0, column=0, padx=4, pady=8)

location_hour = "{city} - {full_date}".format(city=location.city, full_date=moment.full)
place_hour = Label(place_hour_frame, text=location_hour, font='Montserrat 20', fg=ACCENT)
place_hour.grid(row=0, column=0, padx=4, pady=8)

# ------------- GRAPH FRAME -------------

graph_frame = Frame(root, bg='grey')
graph_frame.grid(row=1, column=0, padx=8, pady=8, sticky=NW)

# Create graph list frame
# Plot one graph per row of polluants
for i in range(PARAM_POLLUANT_ROWS):
    graph_item_frame = Frame(graph_frame, width=400, height=100)
    graph_item_frame.grid(row=i)
    
    # Slice to select only polluants of the row to plot
    start_slice_idx = i * PARAM_COLUMNS

    row_polluants = []
    # if it is not the last row we compute the last index
    # and we slice from start index to the last index
    if i + 1 < PARAM_POLLUANT_ROWS:
        end_slice_idx = start_slice_idx + PARAM_COLUMNS
        row_polluants = environment.polluants[start_slice_idx : end_slice_idx]
    # if it is the last row 
    # we slice from start index to the end of list
    else:
        row_polluants = environment.polluants[start_slice_idx:]

    # Plot graph for polluants in the row
    plot_polluants_history(graph_item_frame, row_polluants)

# ------------- MAIN FRAME -------------

main_frame = Frame(root, height=800, bg=BACKGROUND)
main_frame.grid(row=1, column=1, columnspan=3, padx=8, sticky="NEW")

# Display image in main_frame
image = PhotoImage(file="logo.png")
original_image = image.subsample(3,3)  # resize image using subsample

# Plot one card per general param
# Showing name, value and unit
for idx, param in enumerate(environment.generals):
    row = int(idx / PARAM_COLUMNS)
    column = idx % PARAM_COLUMNS
    
    general_param_frame = Frame(main_frame, width=200, bg=ACCENT)
    general_param_frame.grid(row=row, column=column, padx=5, pady=8, sticky="NSW")
    name = Label(general_param_frame, text=param["name"], font='Montserrat 16', bg=ACCENT, fg=SLATE)
    name.grid(row=0, column=0, padx=14, pady=14, sticky="W")
    name = Label(general_param_frame, text=param["value"], font='Montserrat 32 bold', bg=ACCENT)
    name.grid(row=1, column=0, padx=14, sticky="W")
    void = Label(general_param_frame, text="", width=24, font='Montserrat 0', bg=ACCENT)
    void.grid(row=2, column=0, padx=5, pady=5, sticky="W")
    
# Plot one card per polluant
# Showing name, value and unit
for idx, param in enumerate(environment.polluants):
    row = int(idx / PARAM_COLUMNS) + PARAM_GENERAL_ROWS
    column = idx % PARAM_COLUMNS
    
    general_param_frame = Frame(main_frame, width=160, bg=SECONDARY)
    general_param_frame.grid(row=row, column=column, padx=5, pady=8, sticky="NSW")
    name = Label(general_param_frame, text=param["name"], font='Montserrat 16', bg=SECONDARY, fg=SLATE)
    name.grid(row=0, column=0, padx=14, pady=14, sticky="W")
    name = Label(general_param_frame, text=param["value"], font='Montserrat 32 bold', bg=SECONDARY)
    name.grid(row=1, column=0, padx=14, sticky="W")
    void = Label(general_param_frame, text="", width=24, font='Montserrat 0', bg=SECONDARY)
    void.grid(row=2, column=0, padx=5, pady=5, sticky="W")

root.mainloop()
