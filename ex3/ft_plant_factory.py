class Plant:
    def __init__(self,
                 name: str,
                 starting_height: float,
                 days_old: int) -> None:
        self.name = name
        self.height = starting_height
        self.days_old = days_old

    def grow(self, growth_rate: float) -> None:
        self.height = self.height + growth_rate

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height:.1f}cm,\
 {self.days_old} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    plants = [plant1, plant2, plant3, plant4, plant5]

    for plant in plants:
        plant.show()
