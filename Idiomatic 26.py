# Harmful

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_odd(number):
return number % 2 == 1
odd_numbers = filter(is_odd, the_list)
odd_numbers_times_two = list(map(lambda x: x * 2,
odd_numbers))


# Idiomatic

the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers_times_two = [n * 2 for n in the_list if n % 2 ==
1]
