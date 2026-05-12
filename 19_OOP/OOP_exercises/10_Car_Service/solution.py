"""Car service module."""


class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """Initialize Car."""
        self.color = color
        self.make = make
        self.engine_size = engine_size


class Service:
    """Represent car service model."""

    def __init__(self, name: str, max_car_num: int):
        """Initialize Service."""
        self.name = name
        self.max_car_num = max_car_num
        self.queue = []

    def can_add_to_service_queue(self, car: Car) -> bool:
        """Check if it is possible to add car to service queue."""
        if len(self.queue) >= self.max_car_num:
            return False
        for existing_car in self.queue:
            if existing_car.color == car.color and existing_car.make == car.make:
                return False
        return True

    def add_car_to_service_queue(self, car: Car):
        """Add car to service if it is possible."""
        if self.can_add_to_service_queue(car):
            self.queue.append(car)

    def get_service_cars(self) -> list:
        """Get all cars in service."""
        return self.queue

    def repair(self) -> Car:
        """Repair car in service queue."""
        if not self.queue:
            return None
        special_car = next((c for c in self.queue if len(c.color + c.make) == 13), None)
        car_to_repair = special_car if special_car else self.queue[0]
        self.queue.remove(car_to_repair)
        return car_to_repair

    def get_the_car_with_the_biggest_engine(self) -> list:
        """Return a list of cars with the biggest engine size."""
        if not self.queue:
            return []
        max_size = max(car.engine_size for car in self.queue)
        return [car for car in self.queue if car.engine_size == max_size]