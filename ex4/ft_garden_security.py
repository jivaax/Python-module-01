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
        print(f"{self.name}: {self.get_height():.1f}cm, "
              f"{self.get_age()} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(20)
    print(f"\nHeight updated: {rose.get_height():g}cm")
    rose.set_age(12)
    print(f"Age updated: {rose.get_age()} days\n")

    rose.set_height(-5)
    rose.set_age(-3)

    print("\nCurrent state:", end=" ")
    rose.show()
