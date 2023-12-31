class human:
      def eat (self):
            print("I can eat vegitables, meals ")
      def work (self):
            print(" I can perform all kind of works")

class men(human):
      def __init__(self,name):
            self.name = name 
            print(f"hi i am {self.name}")
class women(human):
      pass

men_1 = men("akash")
women_1 = women()

men_1.eat()
women_1.work()
