INTEREST, LIMIT = 0.071, 700000.0
deposit = float(input())
years, gain = 0, 0.0

while deposit < LIMIT:
    years += 1
    gain = deposit * INTEREST
    deposit += gain

print(years)
