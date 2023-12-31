class Human:
      def eat (self):
            print("I can eat vegitables, meals ")
      def work (self):
            print(" I can perform all kind of works")

class Men:
      def __init__(self,name):
            self.name = name 
            print(f"hi i am {self.name}")
      def work (self):
            print("Especially i can code well")
            
class Women(Human,Men):
      pass

men_1 = Men("akash")
women_1 = Women("hela")


women_1.work()

