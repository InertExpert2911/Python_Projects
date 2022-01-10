# Varibale to store sum
sum = 0

# Using range(start, end (not included), step)
for number in range(2, 101, 2):
    sum += number
    # print(number,sum)
    
# Printing total sum    
print(sum)


# Another way can be:

"""
sum = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum += number

print(sum)

"""