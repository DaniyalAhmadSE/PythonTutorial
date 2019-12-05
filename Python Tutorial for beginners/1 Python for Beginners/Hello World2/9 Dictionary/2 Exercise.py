digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ""

phone = input("Phone: ")

for digit in phone:
    output += digits.get(digit, "!") + " "

print(output)
