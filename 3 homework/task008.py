class Backpack:
    def __init__(self, weight_capacity):
        self.list_of_items = []
        self.weight_capacity = weight_capacity

    def empty(self):
        self.list_of_items.clear()

    def put(self, item):
        if item.weight < (self.weight_capacity - self.sum_of_weights()):
            self.list_of_items.append(item)
            return 'You\'ve put your ' + item.name + ' in the backpack!'
        else:
            print("You won\'t be able to raise up your backpack if you\'ll put " + item.name + " in it, so put off something else at first!")

    def count_items(self):
        return len(self.list_of_items)

    def sum_of_weights(self):
        total_weight = 0
        for i in range(self.count_items()):
            total_weight += self.list_of_items[i].weight
        return total_weight

    # ниже метод для красивого вывода списка предметов в рюкзаке, который не особо нужен, поскольку отдельно
    # написан итератор. но красиво, так что удалять не буду.
    # def list_of_items_method(self):
    #     ans = 'Your backpack contains:' + '\n'
    #     items_amount = self.count_items()
    #     if items_amount > 0:
    #         for i in range(items_amount):
    #             ans += "* " + self.list_of_items[i].name + '\n'
    #     else:
    #         return "Now your backpack is empty!"
    #     return ans

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.count_items():
            that_item = self.list_of_items[self.index]
            self.index += 1
            return that_item
        else:
            raise StopIteration


class Item:
    def __init__(self, name,  weight):
        self.name = name
        self.weight = weight

    def rename(self, new_name):
        self.name = new_name


bp1 = Backpack(10)

food_container = Item('a food container', 2)
bottle_of_water = Item('a bottle of water', 1)
laptop = Item('a laptop', 4)
earphones = Item('earphones', 0.5)
book = Item('a book', 2.5)
laptop_charger = Item('a laptop charger', 1)

bp1.put(food_container)
bp1.put(bottle_of_water)
bp1.put(laptop)
bp1.put(earphones)
bp1.put(book)
bp1.put(laptop_charger)
print()

print('here you can check how does the backpack iterator work:')
for i in bp1:
    print(i.name)
