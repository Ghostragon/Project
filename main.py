import numpy as np


# Опитах се да направя пълната имплементация на задачата,
# но не успях да зареждам файлове. Така и не го схванах как да го направя.
# За това реших да въвеждам размерите на матрица, която да се попълва случайно.
def load(file):
    with open(file + ".txt") as f:
        data = f.readlines()
    res = []
    for row in data:
        res.append([])
        for element in row:
            if element != "\n" and element != " ":
                res[-1].append(element)

    return res


a = int(input("Enter rows: "))
b = int(input("Enter columns: "))
rgb = ["R", "G", "B"]
T = [[0 for col in range(b)] for row in range(a)]

for row in range(a):
    for col in range(b):
        T[row][col] = np.random.choice(rgb)

for r in T:
    for c in r:
        print(c, end=" ")
    print()


def findLargest(data):
    visited = []
    area = []
    length = 0
    movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def recScan(x, y, scanArea):
        visited.append((x, y))
        scanArea.append((x, y))

        for dx, dy in movement:
            newX, newY = x + dx, y + dy
            if newX >= 0 and newY >= 0 and newX < len(data) and newY < len(data[newX]):
                if data[x][y] == data[newX][newY] and (not (newX, newY) in visited):
                    recScan(newX, newY, scanArea)
        return scanArea

    for x in range(len(data)):
        for y in range(len(data[x])):
            if (x, y) not in visited:
                newArea = recScan(x, y, [])
                if len(newArea) > length:
                    length = len(newArea)
                    area = newArea
    return length, area


if __name__ == "__main__":
    print(findLargest(T))
