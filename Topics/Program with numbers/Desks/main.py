DESK_CAPACITY = 2

first_group = int(input())
second_group = int(input())
third_group = int(input())

desks_required = (first_group // DESK_CAPACITY) + (first_group % DESK_CAPACITY)
desks_required += (second_group // DESK_CAPACITY) + (second_group % DESK_CAPACITY)
desks_required += (third_group // DESK_CAPACITY) + (third_group % DESK_CAPACITY)

print(desks_required)
