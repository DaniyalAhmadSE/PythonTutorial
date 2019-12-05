try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Error! Age cannot be 0...')
except ValueError:
    print('Error! Invalid value...')
