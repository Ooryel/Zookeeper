duration = int(input())
food = int(input())
flight = int(input())
hotel = int(input())
cost = food * duration
cost += flight * 2
cost += hotel * (duration - 1)
print(cost)
