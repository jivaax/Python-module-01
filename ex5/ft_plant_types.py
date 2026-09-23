class Plant:
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int) -> None:
        self.name = name
        if starting_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = starting_height

        if days_old < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._days_old = 0
        else:
            self._days_old = days_old

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days_old = age

    def grow(self, growth_rate: float) -> None:
        self.set_height(self.get_height() + growth_rate)

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int,
                 color: str) -> None:
        super().__init__(name, starting_height, days_old)
        self.color = color
        self.has_bloomed = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self.has_bloomed:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, starting_height, days_old)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int,
                 harvest_season: str) -> None:
        super().__init__(name, starting_height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def grow(self, growth_rate: float) -> None:
        super().grow(growth_rate)
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()

    print(f"[asking the {flower.name} to bloom]")
    flower.bloom()

    flower.show()

    print("\n=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()

    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("tomato", 5.0, 10, "April")
    vegetable.show()

    print(f"[make {vegetable.name} grow and age for 20 days]")
    for _ in range(20):
        vegetable.grow(2.1)
        vegetable.age()
    vegetable.show()
