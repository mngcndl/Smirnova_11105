# Вариант 3

class NewIterator:
    def __init__(self, st: str, n: int):
        self.st = st
        self.n = n

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count == len(self.st):
            self.st = self.st[::-1]
            self.count = 0
        ans = self.st[self.count]
        self.count += 1
        return ans


MyIterator = NewIterator('mythic', 20)
for i in MyIterator:
    print(i)
