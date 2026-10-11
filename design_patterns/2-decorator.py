#!/usr/bin/env python3

class Coffee:
    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator:
    def __init__(self, inner):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator:
    def __init__(self, inner):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator:
    def __init__(self, inner):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main():
    c1 = MilkDecorator(Coffee())
    print(f"{c1.description()} {c1.cost()}")

    c2 = MilkDecorator(SugarDecorator(Coffee()))
    print(f"{f'{c2.description()} {c2.cost()}'}")

    c3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(f"{c3.description()} {c3.cost()}")


if __name__ == "__main__":
    main()
