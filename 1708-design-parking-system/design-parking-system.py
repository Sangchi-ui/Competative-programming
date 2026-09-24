class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big_cars = big
        self.medium_cars = medium
        self.small_cars = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big_cars > 0:
                self.big_cars -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.medium_cars > 0:
                self.medium_cars -= 1
                return True
            else:
                return False
        if carType == 3:
            if self.small_cars > 0:
                self.small_cars -= 1
                return True
            else:
                return False
        return False
