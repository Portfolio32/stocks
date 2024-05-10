import torch
import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt

def slope(date : int, data: torch.tensor):
    date -= 1
    volumes = []
    dates = []
    for i in range(0,-50,-1):
        volumes.append(data[0, date + i])
        dates.append(date + i)
    return volumes, dates


d = {}
with open("data.csv") as file:
    next(file)
    file = file
    reader = csv.reader(file)
    costs = []
    for line in reader:
        # date is index 0, volume is index 2, open is index 3
        time = dt.strptime(line[0], '%m/%d/%Y').timetuple().tm_yday
        volume = line[2]
        # Accumulating the volumes in the value(list) 
        if d.get(time) == None:
            d[time] = d.get(time, [])
        d.get(time).append(volume)
        costs.append(line[3])
# I want to train my model after the 1500th sets cause at those dates tesla stockhave a pattern
d = list(sorted(d.items()))
T = torch.zeros((1,366), dtype=torch.int32)

for volumes in d:
    number_volumes = len(volumes[1])
    mean_volume = round(sum(int(volume) for volume in volumes[1])/number_volumes)
    date = volumes[0]
    T[0, date-1] = mean_volume


# I can simply assume that if the volumes increase, the price probably decreases
# I can simply assume that if the volume decreases, the price probably increases
# so volumes should be the x value, cause the slope is the rate of change

volumes, dates = slope(366, T)

xs = sum(volume.data for volume in volumes)/50
ys = sum(dates)/50
xys = 



