# Save the input in this variable
ticket = list(input())
digits = list(map(int, ticket))

left = sum(digits[:3])
right = sum(digits[3:])

# Thanks to you, this code will work
if left == right:
    print("Lucky")
else:
    print("Ordinary")
