def even_numbers(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            return i
nums = [1, 2, 3, 4, 5, 6]
for n in even_numbers(nums):
    print(n)