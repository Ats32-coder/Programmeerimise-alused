import random

"""Kontrolltöö 3 OOP"""

class House:
    """Represents a standard house."""
    house_count = 0

    def __init__(self, rooms, address, floors):
        """Initialize house with rooms, address, and floors."""
        self.rooms = rooms
        self.address = address
        self.floors = floors
        House.house_count += 1

    def house_info(self):
        """Print details of the house."""
        print(f"House: {self.address}, Floor: {self.floors}, Room: {self.rooms}")

    def renovate(self, new_rooms):
        """Update the number of rooms if the input is valid."""
        if isinstance(new_rooms, int) and new_rooms > 0:
            self.rooms = new_rooms
            print(f"Renovated! New room count at '{self.address}': {self.rooms}")
        else:
            print(f"Error: Room number must be a positive integer.")

    def house_value(self):
        """Calculate and return the market value of the house."""
        value = self.rooms * 20000 + (self.floors * 5000)
        return value


class Cottage(House):
    """Represents a cottage, inheriting from House."""
    def __init__(self, address, rooms=3, floors=1, is_winter_ready=False):
        """Initialize cottage with winter readiness status."""
        super().__init__(rooms, address, floors)
        self.is_winter_ready = is_winter_ready

    def prepare_for_winter(self):
        """Enable winter readiness for the cottage."""
        if self.is_winter_ready:
            print(f"Cottage at '{self.address}' is already winter-proof.")
        else:
            self.is_winter_ready = True
            print(f"Cottage at '{self.address}' has been prepared for winter.")

    def cottage_value(self):
        """Calculate and return the value of the cottage."""
        base_value = self.rooms * 7000
        if self.is_winter_ready:
            base_value += 5000
        return base_value


if __name__ == '__main__':
    h1 = House(4, "Kase 5", 2)
    h1.house_info()
    h1.renovate(-1)
    h1.renovate(6)
    print(f"Value: ${h1.house_value()}")

    c1 = Cottage("Petsi tee 3", is_winter_ready=False)
    c1.house_info()
    print(f"Cottage Value: ${c1.house_value()}")
    c1.prepare_for_winter()

    print(f"\nTotal houses created: {House.house_count}")

    all_buildings = []
    for i in range(100):
        if i < 60:
            all_buildings.append(House(random.randint(2, 6), f"Street {i}", random.randint(1, 3)))
        else:
            all_buildings.append(Cottage(f"Järvevana tee {i}", random.randint(1, 3), 1))

    total_value = sum(obj.house_value() for obj in all_buildings)

    print(f"Total items: {len(all_buildings)}")
    print(f"Total value of all houses: ${total_value}")
