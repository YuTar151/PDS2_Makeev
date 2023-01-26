"""
Написати програму, яка приймає назву товару і його вартість, після чого записує ці значення у словник.
Довжина словника - 32. Кожен елемент словника - буква української абетки. Врахувати можливість виникнення колізій.
"""

# Creating an empty dictionary with a fixed size of 32
data = {}


def insert_data(item, price):
    key = hash(item) % 32  # Generating a key using the hash function and taking modulo of 32
    if key in data:
        # Handling collision by appending the new item to the list at the key
        data[key].append((item, price))
    else:
        data[key] = [(item, price)]


# Example usage
insert_data("Товар 1", 100)
insert_data("Товар 2", 200)


