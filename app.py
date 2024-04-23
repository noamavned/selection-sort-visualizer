import matplotlib.pyplot as plt
import numpy as np
import time
import random

def gen(n):
    return [random.randint(-5000, 5000) for i in range(n)]

def sug(lst: list[int], t:int = -1, c: int = -1):
    plt.clf()
    x_coords = np.arange(len(lst))
    colors = ['white'] * len(lst)
    if c > -1:
        colors[c] = 'red'
        colors[c - 1] = 'white'
    elif c == -2:
        colors = ['red'] * len(lst)
    plt.bar(x_coords, lst, width=1, color=colors)
    plt.xticks(x_coords, [""] * len(lst))
    plt.yticks([], [])
    plt.gca().set_facecolor('black')
    if t != -1:
        time.sleep(t)
    plt.pause(0.001)

def visualizeList(l: list[int] = gen(15), t: float = 0.0000000000000000001):
    plt.ion()
    fig = plt.figure(figsize=(8, 6))
    sug(l, 1)
    for i in range(len(l)):
        m = None
        for j in range(i, len(l)):
            sug(l, t, j)
            if m is None or l[m] > l[j]:
                m = j
        l.insert(i, l.pop(m))
    sug(l, -1, -2)
    plt.ioff()
    plt.show()

# Test
if __name__ == '__main__':
    visualizeList()
