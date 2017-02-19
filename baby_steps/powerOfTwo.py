"""
    Returns an array of powered numbers by the amount of times it has to be applied.

    @:arg   {Integer}    amount   the number of times the power has to be applied
    @:returns {Array}
"""
def powers_of_two(amount):
    powerArray = []

    for i in range(0, amount + 1):
        powerArray.append(2**i)

    return powerArray

print(powers_of_two(2))