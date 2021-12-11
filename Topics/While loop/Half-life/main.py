initial, final = int(input()), int(input())

delta, period = 0, 12
while initial >= final:
    delta += 1
    initial //= 2

print(delta * period)
