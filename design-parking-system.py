'''
Example 1:

Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
'''


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small         
        

    def addCar(self, carType: int) -> bool:
        #car type = 1, 2, 3
        if carType == 1:
            if self.big >= 1:
                self.big-=1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium-=1
                return True
            else:
                return False
        elif carType == 3:
            if self.small >= 1:
                self.small-=1
                return True        
            else:
                return False
        return False

if __name__ == "__main__":
    parkingSystem = ParkingSystem(1,1,0)
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(1))