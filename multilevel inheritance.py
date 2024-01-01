class human:
      def eat(self):
            print (" I can eat")
      def work (self ):
            print (" I cxan work")
class man(human):
      def sleep (self):
            print (" i can sleep")
class boy (man):
      def work (self):
            super().work()
            print (" I can code ")

boy_1 = boy()
boy_1.work()