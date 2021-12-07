import numpy as np

#test_input = "16,1,2,0,4,2,7,1,2,14"
with open("input.txt", "r") as fh:
    data_input = fh.read()

data = np.array(list(map(int,data_input.split(","))))

fuel_list = []

for i in range(len(data)):
    target = data[i]
    tmp = data[:]
    fuel = sum(abs(tmp - target))
    fuel_list.append(fuel)

print(f"Part 1 minimum fuel: {min(fuel_list)}")

fuel_list = []
for i in range(len(data)):
    target = data[i]
    tmp = data[:]
    distance = abs(tmp-target)
    scale = lambda x: (x*(x+1))/2
    fuel_cost = sum(scale(distance))
    fuel_list.append(fuel_cost)

print(f"Part 2 minimum fuel: {min(fuel_list)}")


