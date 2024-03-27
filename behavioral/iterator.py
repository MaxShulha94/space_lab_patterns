class MyIterator:
    def __init__(self, collection: list = None, _even: bool = False):
        self._collection = collection
        self._index = 0
        self._even = _even

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 2 if self._even else 1
            return value
        except IndexError:
            raise StopIteration()




class IterableCollection:
    def __init__(self):
        self._collection = []

    def add_item(self, item):
        self._collection.append(item)

    def to_iterate(self):
        return MyIterator(self._collection)

    def to_iterate_even(self):
        return MyIterator(self._collection, True)

    def __str__(self):
        return str(self._collection)


collection = IterableCollection()
collection.add_item("Item 1")
collection.add_item("Item 2")
collection.add_item("Item 3")
collection.add_item("Item 4")
collection.add_item("Item 5")
collection.add_item("Item 6")
collection.add_item("Item 7")
collection.add_item("Item 8")


print("Iterating through the collection:")

print("\n".join(collection.to_iterate()), end="\n")
print("Iterating even indexes through the collection:")
print("\n".join(collection.to_iterate_even()), end="\n")

print(collection.__str__())


























