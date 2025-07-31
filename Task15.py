limit = int(input("Enter the upper limit: "))
total = 0
for i in range(1, limit + 1):
    if i % 3 == 0:
        total += i
print(f"\nSum of numbers divisible by 3 from 1 to {limit} is: {total}")
