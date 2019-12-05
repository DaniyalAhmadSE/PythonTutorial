price_of_house = 1000000
buyer_has_good_credit = True

if buyer_has_good_credit:
    down_payment = (price_of_house * 10) / 100

else:
    down_payment = (price_of_house * 20) / 100

print(f'Down payment: ${down_payment}')
