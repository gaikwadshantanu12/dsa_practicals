"""
Implement all the functions of a dictionary (ADT) using hashing and handle collisions using chaining with / without replacement.
Data: Set of (key, value) pairs, Keys are mapped to value, Keys must be comparable, Keys must be unique.
Standard Operations : Insert(key, value), Find(key), Delete(key)
"""

import numpy as np


class HashTableWithReplacement:

    def __init__(self, size):
        self.size = size
        self.chain = np.array([0] * self.size)
        self.hashtable = np.array([0] * self.size)

    def insert(self, key):
        index = int(key % table_size)
        start = index

        if self.hashtable[start] == 0:
            self.chain[start] = -1
            self.hashtable[start] = key
        elif self.hashtable[index] % table_size == key % table_size:
            # Implementing linear probing
            while self.hashtable[start] != 0:
                start = (start + 1) % table_size
            if self.chain[index] == -1:
                self.chain[start] = -1
                self.chain[index] = start
            else:
                for x in range(len(self.hashtable)):
                    if self.hashtable[x] % table_size == key % table_size and self.chain[x] == -1:
                        self.chain[x] = start
                    x += 1

            self.chain[start] = -1
            self.hashtable[start] = key
        else:
            j = start
            while self.hashtable[j] != 0:
                j = (j + 1) % table_size

            i = self.hashtable[start] % table_size
            while self.chain[i] != start:
                i = self.chain[i]
            self.chain[i] = self.chain[start]
            while self.chain[i] != -1:
                i = self.chain[i]
            self.chain[i] = j
            self.hashtable[j] = self.hashtable[index]
            self.chain[j] = -1
            self.hashtable[index] = key
            self.chain[start] = self.chain[index]
            self.chain[index] = -1

    def delete(self, key):
        k = key % table_size
        start = k
        m = 0
        while m != table_size:
            if self.hashtable[k] == key:
                print("Deleted")
                if self.chain[k] == -1:
                    self.chain[k] = -1
                else:
                    while self.chain[start] != k:
                        start = self.chain[start]
                    self.chain[start] = self.chain[k]
                self.chain[k] = -1
                self.hashtable[k] = 0
            else:
                k = (k + 1) % table_size

            m += 1

    def search(self, key):
        k = key % table_size
        m = 0
        i = 1.1
        while m != table_size:
            if self.hashtable[k] == key:
                i = k
            else:
                k = (k + 1) % table_size
            m += 1
        if i != 1.1:
            print(key, " is present at ", i)
        else:
            print(key, " is not present")

    def print_hashtable(self):

        print("Hash table is :-\n\nindex \t value\tchain")
        for x in range(len(self.hashtable)):
            if self.hashtable[x] != 0:
                print(x, "\t", self.hashtable[x], "\t", self.chain[x])
            else:
                print(x, "\t----\t----")


class HashTableWithoutReplacement:

    def __init__(self, size):
        self.size = size
        self.chain = np.array([0] * self.size)
        self.hashtable = np.array([0] * self.size)

    def insert(self, key):
        start = int(key % table_size)

        if self.hashtable[start] == 0:
            self.chain[start] = -1
            self.hashtable[start] = key
        elif self.hashtable[start] % table_size == key % table_size:
            count = 0
            j = start + 1
            while self.hashtable[j] != 0 and count < table_size:
                j = (j + 1) % table_size
                count += 1
            while self.chain[start] != -1:
                start = self.chain[start]
            self.hashtable[j] = key
            self.chain[j] = -1
            self.chain[start] = j
        else:
            count = 0
            j = start
            while self.hashtable[j] != 0:
                j = (j + 1) % table_size
                count += 1
            if count == table_size:
                print("Hash Table Full")
            while self.hashtable[start] % table_size != j and start <= j:
                if self.hashtable[start] % table_size == key % table_size:
                    if self.chain[start] == -1:
                        self.chain[start] = j
                start += 1
            self.hashtable[j] = key
            self.chain[j] = -1

    def delete(self, key):
        k = int(key % table_size)
        start = k
        m = 0
        while m != table_size:
            if self.hashtable[k] == 0:
                print("Not Found")
            elif self.hashtable[k] == key:
                print("Deleted")
                if self.chain[k] == -1:
                    self.chain[k] = -1
                else:
                    while self.chain[start] != k:
                        start = self.chain[start]
                    self.chain[start] = self.chain[k]
                    self.chain[k] = -1
                    self.hashtable[k] = 0
                break
            else:
                k = (k + 1) % table_size
            m += 1

    def search(self, key):
        k = key % table_size
        m = 0
        i = 1.1
        while m != table_size:
            if self.hashtable[k] == key:
                i = k
            else:
                k = (k + 1) % table_size
            m += 1
        if i != 1.1:
            print(key, " is present at ", i)
        else:
            print(key, " is not present")

    def print_hashtable(self):

        print("Hash table is :-\n\nindex \t value\tchain")
        for x in range(len(self.hashtable)):
            if self.hashtable[x] != 0:
                print(x, "\t", self.hashtable[x], "\t", self.chain[x])
            else:
                print(x, "\t----\t----")


if __name__ == "__main__":
    table_size = int(input("Enter table size: "))
    HT = HashTableWithReplacement(table_size)
    HT_no = HashTableWithoutReplacement(table_size)
    print("1. Insert with Replacement\n2. Delete with Replacement\n3. Display with Replacement\n4. Search with "
          "Replacement\n5. Insert without Replacement\n6. Delete without Replacement\n7. Display without "
          "Replacement\n8. Search without Replacement\n9. Exit")
    while 1:
        ch = int(input("Choice: "))
        if ch == 1:
            x = int(input("Enter element: "))
            HT.insert(x)
        elif ch == 2:
            key = int(input("Enter element: "))
            HT.delete(key)
        elif ch == 3:
            HT.print_hashtable()
        elif ch == 4:
            key = int(input("Enter element: "))
            HT.search(key)
        elif ch == 5:
            x = int(input("Enter element: "))
            HT_no.insert(x)
        elif ch == 6:
            key = int(input("Enter element: "))
            HT_no.delete(key)
        elif ch == 7:
            HT_no.print_hashtable()
        elif ch == 8:
            key = int(input("Enter element: "))
            HT_no.search(key)
        elif ch == 9:
            print("Exiting...")
            exit(0)