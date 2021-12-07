import numpy as np

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

# data = test_input.split("\n")

with open("input.txt", "r") as fh:
    data = fh.read().splitlines()

## Make 1000 x 1000 grid, because yolo and cba to find max x and y
matrix = np.zeros((1000,1000))
for t in data:
    points = [i.split(",") for i in t.split(" -> ")]
    x1, y1 = [int(i) for i in points[0]]
    x2, y2 = [int(i) for i in points[1]]
    if y1 == y2:# horizontal line
        start = min([x1, x2])
        end = max([x1,x2]) + 1
        for x in range(start,end):
            matrix[y1][x] += 1
    elif x1 == x2:# vertical
        start = min([y1, y2])
        end = max([y1, y2]) + 1
        for y in range(start, end):
            matrix[y][x1] += 1

print(f"Part 1: {len(matrix[matrix>1])}")


# Part 2
## Make 1000 x 1000 grid, because yolo and cba to find max x and y
matrix = np.zeros((1000,1000))
for t in data:
    points = [i.split(",") for i in t.split(" -> ")]
    x1, y1 = [int(i) for i in points[0]]
    x2, y2 = [int(i) for i in points[1]]
    if y1 == y2:# horizontal line
        start = min([x1, x2])
        end = max([x1,x2]) + 1
        for x in range(start,end):
            matrix[y1][x] += 1
    elif x1 == x2:# vertical
        start = min([y1, y2])
        end = max([y1, y2]) + 1
        for y in range(start, end):
            matrix[y][x1] += 1
    elif abs(x1-x2) == abs(y1-y2): #If you're reading this Rory or Alex ..... FIGHT ME
        if x1 > x2:
            x_points = [i for i in range(x1,x2-1, -1)]
        else:
            x_points = [i for i in range(x1,x2+1)]
        if y1 > y2:
            y_points = [i for i in range(y1,y2-1, -1)]
        else:
            y_points = [i for i in range(y1,y2+1)]
        for i in range(len(x_points)):
            y = y_points[i]
            x = x_points[i]
            matrix[y][x] += 1


print(f"Part 2: {len(matrix[matrix>1])}")