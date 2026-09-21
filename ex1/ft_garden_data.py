class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 50, 70)
    tulip = Plant("Tulip", 30, 40)
    sunflower = Plant("Sunflower", 150, 20)
    daisy = Plant("Daisy", 25, 10)

    rose.show()
    tulip.show()
    sunflower.show()
    daisy.show()
