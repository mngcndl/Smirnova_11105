from abc import abstractmethod, ABC


class Website(ABC):
    def __init__(self, name, countries, user_list):
        self.name = name
        self.countries = countries
        self.user_list = user_list

    @abstractmethod
    def website_presentation(self):
        pass

    def amount_of_users(self):
        return len(self.user_list)

    def countries_list(self):
        countries_list = 'Our website can be used in '
        for i in range(len(self.user_list) - 1):
            countries_list += self.countries[i] + ', '
        countries_list += self.countries[-1] + '.'
        return countries_list


"""Task001b"""


class Webpage:
    def __init__(self, main_color, font, is_the_font_bold: bool):
        self.main_color = main_color
        self.font = font
        self.is_the_font_bold = is_the_font_bold

    def change_page_main_color(self, new_color):
        self.main_color = new_color
        return "Now this webpage\'s new main color is " + new_color

    def change_font(self, new_font):
        self.font = new_font
        return "Now this webpage\'s new font color is " + new_font


class SocialNetwork(Website, Webpage):
    # новый атрибут класса-наследника - owner
    def __init__(self, name, countries, user_list, main_color, font, is_the_font_bold, owner):
        Website.__init__(self, name, countries, user_list)
        Webpage.__init__(self, main_color, font, is_the_font_bold)
        self.owner = owner

    # новые методы класса-наследника - add_user и remove_user
    def add_user(self, user):
        self.user_list.append(user)
        return 'User ' + str(user.name) + ' has been added successfully!'

    def remove_user(self, user):
        self.user_list.pop(self.user_list.index(user))
        return 'User\'s ' + str(user.name) + ' account has been removed successfully!'

    # реализация абстрактного родительского метода
    def website_presentation(self):
        users_str = ''
        for i in range(len(self.user_list) - 1):
            users_str += self.user_list[i].name + ', '
        users_str += self.user_list[-1].name + '.'

        presentation = 'Hello, this is \"' + self.name + '\" social network. ' + "\n" + \
                       'We\'ve got ' + str(self.amount_of_users()) + ' users for now.' + "\n" + \
                       'Their names are ' + users_str + "\n" + self.countries_list() + "\n" + 'Thank you for your attention!'
        return presentation

    # переопределение родительского неабстрактного метода
    def change_page_main_color(self, new_color):
        message = "Main color change is not allowed as you are not the " + self.name + " main designer! So the " + \
                  str(new_color) + " won\'t be the main color of this social network."
        return message


class User:
    def __init__(self, name, surname, password):
        self.name = name
        self.surname = surname
        self.password = password


if __name__ == '__main__':
    ivanPetrov = User('Ivan', 'Petrov', 'this_is_my_password')
    kseniaPetrova = User("Ksenia", "Petrova", 'tamtam')
    erastFandorin = User("Erast", "Fandorin", "KillAzazel")
    masahiroSibata = User("Masa", "Sibato", "ex_yakuza")

    vk = SocialNetwork(name='VK', countries=['Russia', 'Italy', 'France', 'England'], user_list=[],
                       main_color='#4C75A3', font='VK Sans', is_the_font_bold=False, owner='mail.ru')

    instagram = SocialNetwork(name='Instagram', countries=['Russia', 'Germany', 'Norway', 'Sweden'], user_list=[],
                              main_color='#8a3ab9', font='Neue Helvetica', is_the_font_bold=True, owner='Meta')

    list_of_social_networks = [vk, instagram]

    print(vk.add_user(ivanPetrov))
    print(vk.add_user(erastFandorin) + '\n')

    instagram.add_user(kseniaPetrova)
    instagram.add_user(erastFandorin)
    instagram.add_user(masahiroSibata)

    print(vk.website_presentation() + "\n")
    print(instagram.website_presentation() + '\n')
    print(instagram.change_page_main_color('#00FF00'))
