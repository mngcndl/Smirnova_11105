from abc import abstractmethod, ABC


class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_value(self, value):
        self.__value = value

    def set_next(self, value):
        new_node = Node(value)
        self.__next = new_node


class AbstractList(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def pop(self, *args):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def append_list(self, this_list):
        pass

    @abstractmethod
    def clear(self):
        pass


class LinkedStack(AbstractList):
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ''
        elem = self.head
        if self.head is None:
            return "This list is empty now"
        else:
            while elem is not None:
                if elem.get_next() is None:
                    result += str(elem.get_value())
                else:
                    result += str(elem.get_value()) + ' -> '
                elem = elem.get_next()
        return result

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            tek = self.head
            while tek.get_next() is not None:
                tek = tek.get_next()
            tek.set_next(value)

    def __len__(self):
        tek = self.head
        l = 0
        if tek is not None:
            l += 1
            while tek.get_next() is not None:
                tek = tek.get_next()
                l += 1
        return l

    def pop(self):
        if self.head is None:
            return None
        else:
            tek = self.head
            while tek.get_next().get_next() is not None:
                tek = tek.get_next()
            elem = tek.get_next().get_value()
            tek.set_next(None)
        return elem

    def append_list(self, this_list):
        tek = self.head
        if this_list:
            if tek is not None:
                while tek.get_next() is not None:
                    tek = tek.get_next()
            for i in range(len(this_list)):
                tek.set_next(this_list)
                tek = tek.get_next()
        return self.__str__()

    def clear(self):
        self.head = None


class LinkedDeque(AbstractList):
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ''
        elem = self.head
        while elem is not None:
            result += str(elem) + ' -> '
            elem = elem.get_next()
        result += 'None'
        return result

    def append(self, value): #equals to push_back
        if self.head is None:
            self.head = Node(value)
        else:
            tek = self.head
            while tek.get_next() is not None:
                tek = tek.get_next()
            elem = tek
            elem.set_next(value)
            elem.get_next().set_next(tek.get_next())

    def push_front(self, value):
        hhead = self.head
        new_head = Node(value)
        new_head.set_next(hhead)
        self.head = new_head

    def pop(self, elem):
        tek = self.head
        if tek is None and elem is not None:
            return "there/'s no such an element in this deque"
        else:
            while tek.get_next() != elem:
                tek = tek.get_next()
            elem = tek.get_next().get_value()
            tek.set_next(tek.get_next().get_next())
            return elem

    def __len__(self):
        counter = 0
        tek = self.head
        if tek is not None:
            while tek.get_next() is not None:
                tek = tek.get_next()
                counter += 1
        return counter

    def append_list(self, this_list):
        tek = self.head
        if this_list:
            if tek is not None:
                while tek.get_next() is not None:
                    tek = tek.get_next()
            for i in range(len(this_list)):
                tek.set_next(this_list)
                tek = tek.get_next()
        return self.__str__()

    def clear(self):
        self.head = None


class LinkedSet(AbstractList):
    def __init__(self):
        self.head = None

    def __str__(self):
        result = ''
        elem = self.head
        while elem is not None:
            result += str(elem) + ' -> '
            elem = elem.get_next()
        result += 'None'
        return result

    def append(self, value):
        tek = self.head
        while tek.get_value() is not None:
            if tek.get_value() == value:
                return "This element already is in the set."
            if tek.get_next() is None:
                tek.set_next(value)

    def pop(self, value):
        flag = 'Can\'t pop that value, it\'s not in the set.'
        tek = self.head
        if tek is not None:
            while tek.get_next() is not None and flag != "Successfully popped":
                if tek.get_next().get_value() == value:
                    tek.set_next(tek.get_next().get_next())
                    flag = 'Successfully popped'
                tek = tek.get_next()
        return flag

    def __len__(self):
        counter = 0
        tek = self.head
        if tek is not None:
            while tek.get_next() is not None:
                tek = tek.get_next()
                counter += 1
        return counter

    def append_list(self, this_list):
        tek = self.head
        while tek.get_next() is not None:
            tek = tek.get_next()
            if this_list.count(tek.get_value()) > 0:
                this_list.pop()
                
    def clear(self):
        self.head = None
