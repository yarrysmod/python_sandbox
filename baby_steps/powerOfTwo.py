import math

def powers_of_two(n):
    powerArray = [1]

    for i in range(n):
        powered = int(math.pow(2, i + 1))
        powerArray.append(powered)

    return powerArray

def test():
    print powers_of_two(2)

test()