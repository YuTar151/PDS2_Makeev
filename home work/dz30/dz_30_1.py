"""
1. Написати клас для створення і роботи з хеш-таблицями. Клас повинен містити наступні функції:
- створення хеш-таблиці заданої довжини;
- пошук, додавання і видалення нових елементів;
- друкування хеш-таблиці;
- виправлення колізій;
"""


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        key_value = 0
        for char in key:
            key_value += ord(char)
        return key_value % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def print_table(self):
        for i, item in enumerate(self.table):
            print(f'{i}: {item}')

    def resolve_collision(self):
        for index, key_value in enumerate(self.table):
            if len(key_value) > 1:
                for k, v in key_value:
                    new_index = self.hash_function(k)
                    if new_index == index:
                        new_index = self.hash_function(k + 1)
                    self.table[new_index].append((k, v))
                self.table[index] = None


table = HashTable(10)
table.add("UserLogin", "Password123")
table.print_table()
