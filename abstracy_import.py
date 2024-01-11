from abstract import vehicle

class Bike (vehicle):
      def __init__ (self,n,color):
            self.no_of_wheels = n 
            self.color_of_bike = color
      def start(self):
            print("Kick to start")

class Car (vehicle):
      def __init__(self,n,x):
            self.no_of_wheels = n
            self.no_of_gears = x
      def start(self):
            print("key to start")

car = Car(4)
car.start()
