class human:
      def eat(self):
            print("I can eat fruits")
      def work(self):
            print("I can perform any work")


class male (human):
      def work(self):
            print("I can work hard")

male_1 = male()
male_1.eat()
male_1.work()