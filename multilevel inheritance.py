class Human:
      def eat(self):
            print (" I can eat")
      def work (self ):
            print (" I cxan work")
class Man(human):
      def sleep (self):
            print (" i can sleep")
class Boy (man):
      def work (self):
            super().work()
            print (" I can code ")

boy_1 = Boy()
boy_1.work()