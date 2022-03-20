class Buildings:
    def __init__(self, name, purpose, height, holding_capacity, main_material):
        self.name = name
        self.purpose = purpose
        self.height = height
        self.holding_capacity = holding_capacity
        self.main_material = main_material

    def __eq__(self, other):
        res = ''
        if self.purpose == other.purpose:
            res += 'These two buildings were created for the same purpose - as a ' + self.purpose + '\n'
        else:
            res += 'Purposes of those two buildings are different, the ' + self.name + ' was built as a ' + self.purpose \
                   + ', and the ' + other.name + ' - as a ' + other.purpose + '.' + '\n'

        if self.height > other.height:
            res += 'The first building is higher than the second one.' + '\n'
        elif self.height < other.height:
            res += 'The second building is higher than the first one.' + '\n'
        else:
            res += 'Height of two buildings is equal.'

        if self.holding_capacity > other.holding_capacity:
            res += 'The first building can can be visited by more people at the same time than the second one.' + '\n'
        elif self.height < other.height:
            res += 'The second building can can be visited by more people at the same time than the first one.' + '\n'
        else:
            res += 'These two buildings can be visited by the same amount of people at the same time.' + '\n'

        if self.main_material == other.main_material:
            res += 'These buildings are made of the same material.'
        else:
            res += 'Main materials of these buildings are different: the first one is mostly made of ' + self.main_material + \
                   ', and the other one is made of ' + other.main_material + '.'

        return res


igloo = Buildings('Igloo', 'house', 2, 10, 'snow')
skyscrapper = Buildings('Skyscrapper', 'business building', 28, 200, 'concrete')
print(igloo.__eq__(skyscrapper))