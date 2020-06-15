import abc


class Beverage(metaclass=abc.ABCMeta):
    description = 'No Beverage'

    def get_description(self):
        return self.description

    @abc.abstractmethod
    def get_cost(self):
        pass


class CondimentDecorator(Beverage, metaclass=abc.ABCMeta):

    def __init__(self, beverage):
        self._beverage = beverage

    @abc.abstractmethod
    def get_cost(self):
        pass


class Espresso(Beverage):
    def __init__(self):
        self.description = 'This is Espresso'

    def get_cost(self):
        return 0.99


class Mocha(CondimentDecorator):

    def get_description(self):
        return self._beverage.get_description() + ', Mocha'

    def get_cost(self):
        return self._beverage.get_cost() + 0.2


class Whip(CondimentDecorator):

    def get_description(self):
        return self._beverage.get_description() + ', Whip'

    def get_cost(self):
        return self._beverage.get_cost() + 0.8


if __name__ == "__main__":
    myCoffee = Espresso()
    print(myCoffee.get_description())
    print(myCoffee.get_cost())

    coffeeMocha = Mocha(myCoffee)
    print(coffeeMocha.get_description())
    print(coffeeMocha.get_cost())

    coffeeWhip = Whip(myCoffee)
    print(coffeeWhip.get_description())
    print(coffeeWhip.get_cost())

    coffeeMochaWhip = Whip(coffeeMocha)
    print(coffeeMochaWhip.get_description())
    print(coffeeMochaWhip.get_cost())

    coffeeMochaWhip2 = Whip(Mocha(myCoffee))
    print(coffeeMochaWhip2.get_description())
    print(coffeeMochaWhip2.get_cost())
