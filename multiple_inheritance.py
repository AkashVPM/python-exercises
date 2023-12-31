class human:
      def eat (self):
            print("I can eat vegitables, meals ")
      def work (self):
            print(" I can perform all kind of works")

class men(human):
      def __init__(self,name):
            self.name = name 
            print(f"hi i am {self.name}")
      def work (self):
            super().work()
            print("Especially i can code well")
class women(human):
      pass

men_1 = men("akash")
women_1 = women()

men_1.work()
men_1.eat()
women_1.work()

