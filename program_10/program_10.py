list_numbers = [[2,4,5],[4,6,8],[3,6,9]]

print(sum([sum(filter(lambda n: n % 2 == 0, list_numbers[index])) for index in range(len(list_numbers))]))

print(sum([sum(list_numbers[index]) for index in range(len(list_numbers))]))
