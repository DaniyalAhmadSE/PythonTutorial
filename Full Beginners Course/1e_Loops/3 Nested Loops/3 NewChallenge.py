numbers = [1, 1, 1, 1, 6]

for x_count in numbers:
    "print('x' * x_count)"
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
