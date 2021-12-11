HOUR_AS_SECONDS = 3600
MINUTE_AS_SECONDS = 60

departure, rain = 0, 0

departure += int(input()) * HOUR_AS_SECONDS
departure += int(input()) * MINUTE_AS_SECONDS
departure += int(input())

rain += int(input()) * HOUR_AS_SECONDS
rain += int(input()) * MINUTE_AS_SECONDS
rain += int(input())

difference = rain - departure
print(difference)
