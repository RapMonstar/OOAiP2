# Шаблонный метод
# Приготовление 2-х блюд - окрошка и лапша

class Food():
    def addWater(self):
        print('Добавление воды')

    def salt(self):
        print('Добавление соли')

    def vegetables(self):
        pass

    def sausage(self):
        pass

    def pasta(self):
        pass

    def startCook(self):
        self.salt()
        self.addWater()
        self.vegetables()
        self.sausage()
        self.pasta()


class Okroshka(Food):
    def vegetables(self):
        print('Добавление овощей')

    def sausage(self):
        print('Добавление колбаски')


class Noodle(Food):
    def pasta(self):
        print('Добавление макарошек')


if __name__ == '__main__':
    okroshka = Okroshka()
    okroshka.startCook()
    print()
    noodle = Noodle()
    noodle.startCook()