# Harmful

some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, rest) = some_list[0], some_list[1],
some_list[2:]
print(rest)
(first, middle, last) = some_list[0], some_list[1:-1],
some_list[-1]
print(middle)
(head, penultimate, last) = some_list[:-2], some_list[-2],
some_list[-1]
print(head)



# Idiomatic

some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, *rest) = some_list
print(rest)
(first, *middle, last) = some_list
print(middle)
(*head, penultimate, last) = some_list
print(head
