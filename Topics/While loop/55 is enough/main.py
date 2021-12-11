average, count, integer, summation = 0, 0, 0, 0
INVARIANT = 55

while True:
    integer = int(input())

    if integer == INVARIANT:
        break

    count += 1
    summation += integer

average = round(summation / count)
print(count, summation, average, sep="\n")
