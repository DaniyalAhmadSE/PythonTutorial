b = 1


def test(a):
    global b
    a = a + 5
    b = a


# test(b)

print(b)
