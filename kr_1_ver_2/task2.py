# Вариант 5

class ShapeIterator:
    def __init__(self, n: int):
        self.n = n
        if n % 2 == 0:
            self.shape = 'square'
        else:
            self.shape = 'romb'
            self.till_mid = self.n // 2 + 1
            self.iter = 1

    def __iter__(self):
        self.count = 1
        return self

    def __next__(self):
        if self.shape == 'square':
            if self.count <= self.n:
                ans = '*' * self.n
                self.count += 1
                return ans
            else:
                raise StopIteration
        else:
            if self.iter <= self.n:
                ans = ' ' * (self.till_mid - self.count) + "*" * (self.count - 1) + "*" + "*" * (self.count - 1) + ' ' * (self.till_mid - self.count)
                if self.iter >= self.till_mid:
                    self.count -= 1
                else:
                    self.count += 1
                self.iter += 1
                return ans
            else:
                raise StopIteration


Shape1 = ShapeIterator(4)
Shape2 = ShapeIterator(7)

for i in Shape1:
    print(i)
print()
for i in Shape2:
    print(i)
