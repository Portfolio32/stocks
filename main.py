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
    for line in reader:
        # date is index 0, volume is index 2, open is index 3
        time = dt.strptime(line[0], '%m/%d/%Y').timetuple().tm_yday
        volume = line[2]
        # Accumulating the volumes in the value(list) 
        if d.get(time) == None:
            d[time] = d.get(time, [])
        d.get(time).append(volume)
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
predication_day = int(input("Enter number corresponding to date [1-366]: "))
volumes, dates = slope(predication_day, T)
volumes = [int(volume) for volume in volumes]
xs = sum(volume for volume in volumes)
ys = sum(dates)
xys = sum([x*y for x,y in zip(volumes, dates)])
xxs = sum(x**2 for x in volumes)

m = (xys - (xs*ys)/50)/(xxs - xxs/50)

if m > 0:
    print("Price will decrease")
elif m < 0:
    print("Price will increase")
else:
    print("nohting will change")


