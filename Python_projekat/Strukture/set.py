import time


class Set:
    def __init__(self):
        self.data = {}

    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return self.data.__iter__()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        string = '{'
        i = 2
        for value in self.data.keys():
            i = 0
            string = string + str(value) + ','
        return string[:-1 + i] + '}'

    def __or__(self, other):
        if not isinstance(other, Set):
            return NotImplemented
        if len(self) <= len(other):
            smaller = self
            result = other
        else:
            smaller = other
            result = self
        for value in smaller:
            result.add(value)
        return result

    def __and__(self, other):
        if not isinstance(other, Set):
            return NotImplemented
        result = Set()
        if len(self) <= len(other):
            smaller = self
            bigger = other
        else:
            smaller = other
            bigger = self
        for value in smaller:
            if value in bigger:
                result.add(value)
        return result

    def __sub__(self, other):
        if not isinstance(other, Set):
            return NotImplemented
        result = Set()
        for value in self:
            if value not in other:
                result.add(value)
        return result

    def add(self, item):
        try:
            self.data[item] = True
        except TypeError:
            raise

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def remove(self, item):
        try:
            del self.data[item]
        except KeyError:
            print("Ne postoji dati element")

