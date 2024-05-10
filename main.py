import torch
import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

d = {}
with open("data.csv") as file:
    next(file)
    file = file
    reader = csv.reader(file)
    costs = []
    for line in reader:
        # First I would like to get the open part cause it's at the start of the day
        # I'll try graphing date with open + volume using matplotlib.
        # date is index 0, volume is index 2, open is index 3
        time = dt.strptime(line[0], '%m/%d/%Y').timetuple().tm_yday
        volume = line[2]
        if d.get(time) == None:
            d[time] = d.get(time, [])
        d.get(time).append(volume)
        #costs.append(line[3])
# I want to train my model after the 1500th sets cause at those dates tesla stockhave a pattern
d = list(sorted(d.items()))

