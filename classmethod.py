class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is: ', cls.name)

apple = Fruit()
berry = Fruit()

apple.name = 'Apple'
Fruit.printName()
apple.printName()
berry.printName()

Fruit.name = 'Apple'
Fruit.printName()
apple.printName()
berry.printName()