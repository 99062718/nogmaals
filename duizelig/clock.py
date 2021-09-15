ampm = ["AM", "PM"]
time = 0
timeMax = 12

for x in ampm:
    while time < timeMax:
        print(time, x)
        time += 1
    timeMax += 12