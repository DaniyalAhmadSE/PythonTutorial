lis = [1, 1, 2, 4, 5, 'a', 'c', 'a']

for item in lis:
    if lis.count(item) > 1:
        lis.remove(item)
print(lis)
