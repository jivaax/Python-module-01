class Plant:
    def __init__(self, name: str, height: float, days_old: int) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old

    def grow(self, growth_rate: float) -> None:
        self.height = round(self.height + growth_rate, 1)

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    start_height = 10
    age_days = 10
    growth_rate = 0.7
    plant = Plant("Rose", start_height, age_days)
    plant.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant.grow(growth_rate)
        plant.age()
        plant.show()
    week_growth = round(plant.height - start_height, 1)
    print(f"Growth this week: {week_growth}cm")
