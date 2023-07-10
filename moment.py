from datetime import datetime

class Moment():
    day = datetime.now().strftime('%A, %d %B %Y'),
    hour = datetime.now().strftime('%Hh:%M'),
    full = datetime.now().strftime('%A, %d %B %Y %Hh:%M')