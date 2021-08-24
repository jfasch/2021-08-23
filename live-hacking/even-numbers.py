def even_numbers(upper_bound):
    num = 0
    while num < upper_bound:
        if num % 2 == 0:
            yield num
        num += 1

my_even_numbers = even_numbers(100)
for element in my_even_numbers:
    print(element)
