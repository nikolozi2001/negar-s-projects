# Task1 from docs

# names = ['Felix', 'Aaron']
# ages = [19, 16]



# name_one = ['Felix is', 19]
# print(name_one)

# name_two = ['Aaron is', 16]
# print(name_two)

# names_and_ages = [['Felix', 19], ['Aaron', 16]]
# print(names_and_ages)

# nameAndAges = {'Felix':19, 'Aaron':16}
# print(nameAndAges)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)
