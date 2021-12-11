integer = int(input())
summation = integer // 100
summation += (integer // 10) % 10
summation += integer % 10
print(summation)
