weight = input('Enter Weight(in lbs or kg): ')
unit = input('Enter Unit (L(or l) for lbs & K(or k) for kg): ')

if unit == 'l' or unit == 'L':

    converted_weight = round(int(weight) / 2.2046226218, 2)
    print(f'Your weight in kg is {converted_weight}')

elif unit == 'k' or unit == 'K':

    converted_weight = round(int(weight) * 2.2046226218, 2)
    print(f'Your weight in kg is {converted_weight}')

else:

    print('Error!\nPlease make sure you entered everything correctly...')
