class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self._slots[carType] > 0:
            self._slots[carType] -= 1
            return True
        return False
