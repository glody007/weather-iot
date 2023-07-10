# Import Module
from tkinter import *
from data import moment, location, environment
from graph import (
    plot_temperature_history, 
    plot_humidity_history, 
    plot_pm10_history
)

PRIMARY = "#3b82f6"
ACCENT = "#60a5fa"
SECONDARY = "#6ee7b7"
DESTRUCTIVE = "#fda4af" 
BACKGROUND = "#cbd5e1"
SLATE = "#334155"

# create root window
root = Tk()

# root background
root.configure(background=BACKGROUND)

# root window title and dimension
root.title("WEATHER IOT")
# Set geometry(widthxheight)
root.maxsize(1305, 780)
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
graph_frame.grid(row=1, column=0, padx=8, pady=8, sticky="w")

# Create graph list frame
temperature_graph_frame = Frame(graph_frame, width=400, height=185)
temperature_graph_frame.grid(row=2)

humidity_graph_frame = Frame(graph_frame, width=400, height=185)
humidity_graph_frame.grid(row=3)

pm10_graph_frame = Frame(graph_frame, width=400, height=185)
pm10_graph_frame.grid(row=4)

plot_temperature_history(temperature_graph_frame)
plot_humidity_history(humidity_graph_frame)
plot_pm10_history(pm10_graph_frame)


# ------------- MAIN FRAME -------------

main_frame = Frame(root, height=800, bg=BACKGROUND)
main_frame.grid(row=1, column=1, columnspan=3, padx=8, sticky="NEW")

# Display image in main_frame
image = PhotoImage(file="logo.png")
original_image = image.subsample(3,3)  # resize image using subsample

for idx, param in enumerate(environment.generals):
    general_param_frame = Frame(main_frame, width=200, bg=ACCENT)
    general_param_frame.grid(row=0, column=idx, padx=5, pady=8, sticky="NSW")
    name = Label(general_param_frame, text=param["name"], font='Montserrat 16', bg=ACCENT, fg=SLATE)
    name.grid(row=0, column=0, padx=14, pady=14, sticky="W")
    name = Label(general_param_frame, text=param["value"], font='Montserrat 32 bold', bg=ACCENT)
    name.grid(row=1, column=0, padx=14, sticky="W")
    void = Label(general_param_frame, text="", width=24, font='Montserrat 0', bg=ACCENT)
    void.grid(row=2, column=0, padx=5, pady=5, sticky="W")
    
for idx, param in enumerate(environment.polluants):
    row = int(idx/4) + 1
    column = idx % 4
    
    general_param_frame = Frame(main_frame, width=160, bg=SECONDARY)
    general_param_frame.grid(row=row, column=column, padx=5, pady=8, sticky="NSW")
    name = Label(general_param_frame, text=param["name"], font='Montserrat 16', bg=SECONDARY, fg=SLATE)
    name.grid(row=0, column=0, padx=14, pady=14, sticky="W")
    name = Label(general_param_frame, text=param["value"], font='Montserrat 32 bold', bg=SECONDARY)
    name.grid(row=1, column=0, padx=14, sticky="W")
    void = Label(general_param_frame, text="", width=24, font='Montserrat 0', bg=SECONDARY)
    void.grid(row=2, column=0, padx=5, pady=5, sticky="W")

root.mainloop()
