from abc import ABC,abstractmethod
class vehicle(ABC):
      def __init__ (self,n,color):
            self.no_of_wheels = n
      @abstractmethod
      def start(self):
            pass
      def display(self):
            print("I call from the vechicle")

# veh = vehicle(4)
# veh.display()

