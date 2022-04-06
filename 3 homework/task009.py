import folium


class Elephant:
    def __init__(self, color, id, zoo):
        self.color = color
        self.id = id
        self.zoo = zoo

    @classmethod
    def birth_on_the_map(cls, color, id, latitude, longitude):
        map = folium.Map(location=[latitude, longitude], zoom_start=8)
        folium.Marker(location=[latitude, longitude], popup='Here was born a new elephant', icon=folium.Icon(color = 'blue')).add_to(map)
        to_save = "map" + str(id) + ".html"
        map.save(to_save)
        return cls(color, id, map)

    def color_change(self, new_color):
        self.color = new_color

    @staticmethod
    def red_coloured_elephants_counter(lst):
        counter = 0
        for i in range(len(lst)):
            if lst[i].color == 'red':
                counter += 1
        return counter


el1 = Elephant('red', 1, 'Big Zoo in Melbourne')
el2 = Elephant('red', 2, 'Small Zoo in Africa')
el3 = Elephant('grey', 3, 'Big Zoo in Melbourne')

el4 = Elephant.birth_on_the_map('red', 4, 55.75, 37.6167)
print(Elephant.red_coloured_elephants_counter([el1, el2, el3, el4]))
