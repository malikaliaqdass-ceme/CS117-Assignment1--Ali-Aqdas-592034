# B3: Analyses sensor readings in a single loop: count above 3.2 V, highest, lowest, average.
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

above_count = 0
highest = readings[0]
lowest = readings[0]
total = 0
count = 0

for reading in readings:
    if reading > 3.2:
        above_count = above_count + 1
    if reading > highest:
        highest = reading
    if reading < lowest:
        lowest = reading
    total = total + reading
    count = count + 1

average = total / count

print("Readings above 3.2 V:", above_count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 2), "V")
