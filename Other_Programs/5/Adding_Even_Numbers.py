# A variable to hold sum of all even numbers
sum_of_evens = 0

# Use the range(start, end, step) tyo start from 0 till 100 (101 not included, that is how range works) with a step of 2
# So, the range starts from 0, 2, 4, 6,..... (Each step is 2)
for number in range(0, 101, 2):
    # Save the number in the variable defined above
    sum_of_evens += number

# Print the result
print(f"Sum of all even numbers between 1 and 100 is: {sum_of_evens}")