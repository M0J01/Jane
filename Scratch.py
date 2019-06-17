import time

timez = time.localtime()
timeMarker = ''
for item in timez[0:5]:
    timeMarker += "_" + str(item)


print(timeMarker)