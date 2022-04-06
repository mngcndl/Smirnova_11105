from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def presentation_of_the_item(self):
        return "This is " + self.name + " presentation. It will show you some information about this item."

    def change_item_name(self):
        print("Do you want to change item\'s name? Print \'yes\' or \'no\'.")
        if input() == 'yes':
            print('Type item\'s new name below, please!')
            self.name = input()
        else:
            print("Okay.")
        return "Item\'s name now is " + self.name

    def change_item_weight(self):
        print("Do you want to change item\'s weight? Print \'yes\' or \'no\'.")
        if input() == 'yes':
            print('Type item\'s new weight below, please!')
            self.weight = input()
        else:
            print("Okay.")
        return "Item\'s weight now is " + str(self.weight)

    @abstractmethod
    def compare_with_basic_item_of_this_class(self):
        pass

    @abstractmethod
    def where_it_can_be_hold(self):
        pass

    @abstractmethod
    def approximate_characteristic_of_user(self):
        pass

    @abstractmethod
    def how_can_it_be_used(self):
        pass

    def free1(self):
        pass

    def free2(self):
        pass

    def free3(self):
        pass

    def key_method_for_item(self):
        print()
        print(self.presentation_of_the_item())
        self.change_item_name()
        print()
        self.change_item_weight()
        print()
        if self.free1() is not None:
            print(self.free1())
            print()
        print(self.compare_with_basic_item_of_this_class()) #A
        print()
        print(self.where_it_can_be_hold()) #A
        print()
        if self.free2() is not None:
            print(self.free2())
            print()
        print(self.approximate_characteristic_of_user()) #A
        print()
        print(self.how_can_it_be_used()) #A
        print()
        if self.free3() is not None:
            print(self.free3())
            print()


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


class ItemForDailyUsage(Item):
    def __init__(self, name, weight, material):
        super().__init__(name,  weight)
        self.material = material

    def compare_with_basic_item_of_this_class(self):
        print('Basic item of this class is a spoon. Spoon is quite comfortable for eating, it\'s weight is very small '
              '- just 0.1 kg, and it can be made of stainless steel or wood.')
        print("Do you want to know how many spoons your item weights? Print \'yes\' or \'no\' below, please!")
        if input() == 'yes':
            return self.name + " weights like " + str(self.weight / 0.1) + " spoons."
        else:
            'Okay.'

    def where_it_can_be_hold(self):
        print('As long as this is an item for daily usage, it probably can be hold in a backpack.')
        if self.weight < 10:
            return "Seems like it can really be hold in backpack because the weight of " + self.name + \
                   "is less than 10 kilos."
        else:
            return "Oh, this item is too heavy, it can be used just where it stands, like at someone\'s house."

    def approximate_characteristic_of_user(self):
        return "This is an item for daily usage, so it can be used by every person."

    def how_can_it_be_used(self):
        return "Probably, you can use this item at home or at school or anywhere else, because it\'s necessary for most " \
               "of the people."

    def free1(self):
        if self.material == 'plastic':
            return "This item probably is not the best decision because it\'s main material (plastic) is bad for our " \
                   "planet. " \
                   "You can try to find an alternative when " + self.name + " will be used."
        else:
            return "This item is mostly made of " + self.material + "."

    def free2(self):
        return None

    def free3(self):
        return None


class MedicalItem(Item):
    def __init__(self, name, weight, should_it_be_aseptic, max_usage_time):
        super().__init__(name,  weight)
        self.should_it_be_aseptic = should_it_be_aseptic
        self.max_usage_time = max_usage_time

    def compare_with_basic_item_of_this_class(self):
        print('Basic item of this class is a roller-bandage. It\'s weight is small enough '\
              '- just 0.15 kg, and it can be made of textile.')
        print("Do you want to know how many roller-bandages your item weights? Print \'yes\' or \'no\' below, please!")
        if input() == 'yes':
            return self.name + " weights " + str(self.weight / 0.15) + " roller-bandages."
        else:
            'Okay.'

    def where_it_can_be_hold(self):
        return 'As long as this is an item for medical usage, it probably can be hold in a hospital locker.'

    def approximate_characteristic_of_user(self):
        return "This is an item for medical usage, so it can be used by a doctor. Use google to find, " \
               "which doctor usually use " + self.name + "."

    def how_can_it_be_used(self):
        return "Probably, doctor will use it to examine the patient."

    def free1(self):
        return None

    def free2(self):
        if self.should_it_be_aseptic:
            return "This item is probably personal."
        else:
            return "This item can be cleaned and used again."

    def free3(self):
        if self.max_usage_time < '24h':
            return "A doctor will change " + self.name + " after every usage and at every 24 hours."
        else:
            return "This item can be used for the long period of time."


bp1 = Backpack(10)

food_container = ItemForDailyUsage('a food container', 2, 'plastic')
bottle_of_water = ItemForDailyUsage('a bottle of water', 1, 'plastic')
laptop = ItemForDailyUsage('a laptop', 4, 'iron')
earphones = ItemForDailyUsage('earphones', 0.5, 'plastic')
book = ItemForDailyUsage('a book', 2.5, 'paper')
laptop_charger = ItemForDailyUsage('a laptop charger', 1, 'plastic')
pack_of_roller_bandages = MedicalItem('a pack of roller bandages', 1.5, True, '5h')
medical_needle = MedicalItem('a medical needle', 0.001, True, 'a year')

bp1.put(food_container)
bp1.put(bottle_of_water)
bp1.put(earphones)
bp1.put(book)
bp1.put(laptop_charger)
bp1.put(pack_of_roller_bandages)
bp1.put(medical_needle)

print('here you can check how does the backpack iterator work:')
for i in bp1:
    print(i.key_method_for_item())
