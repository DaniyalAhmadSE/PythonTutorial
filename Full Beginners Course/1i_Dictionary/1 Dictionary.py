customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

# print(customer["birth_date"])
# print(customer["Name"])

# print(customer.get("birth_date"))
# print(customer.get("birth_date", "jan 1 1980"))

# customer["name"] = "Jack Smith"
# print(customer["name"])

customer["birth_date"] = "Jan 1 1980"
print(customer["birth_date"])
