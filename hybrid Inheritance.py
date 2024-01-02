class A:
      def show(self):
            print ("drama")
class B(A):
      def movie(self):
            print("lights out")
class C:
      def anime(self):
            print("naruto")
class D(B,C):
      pass

d_1 = D()
d_1.show()