class Plant:
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int) -> None:
        self.name = name
        self._statistics = self.Statistics()
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

    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow_call(self) -> None:
            self._grow_calls += 1

        def add_age_call(self) -> None:
            self._age_calls += 1

        def add_show_call(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

        def add_shade_call(self) -> None:
            pass

    @staticmethod
    def older_than_year(days_old: int) -> bool:
        return days_old > 365

    @classmethod
    def unknown_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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
        self._statistics.add_grow_call()

    def age(self, days: int = 1) -> None:
        self.set_age(self.get_age() + days)
        self._statistics.add_age_call()

    def show(self) -> None:
        self._statistics.add_show_call()
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

    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade_call(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
            )
        self._statistics.add_shade_call()

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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


class Seed(Flower):
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int,
                 color: str) -> None:
        super().__init__(name, starting_height, days_old, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


def stats_for_any_kind(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant._statistics.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")

    print("\n=== Flower")
    flower = Flower("rose", 15.0, 10, "red")
    flower.show()
    stats_for_any_kind(flower)
    print(f"[asking the {flower.name} to grow and bloom]")
    flower.grow(8)
    flower.bloom()
    flower.show()
    stats_for_any_kind(flower)

    print("\n=== Tree")
    tree = Tree("oak", 200.0, 365, 5.0)
    tree.show()
    stats_for_any_kind(tree)
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()
    stats_for_any_kind(tree)

    print("\n=== Seed")
    seed = Seed("sunflower", 80.0, 45, "yellow")
    seed.show()
    print(f"[make {seed.name} grow, age and bloom]")
    seed.grow(30)
    seed.age(20)
    seed.bloom()
    seed.show()
    stats_for_any_kind(seed)

    print("\n=== Anonymous")
    anonymous = Plant.unknown_plant()
    anonymous.show()
    stats_for_any_kind(anonymous)
