class circle:
      pi = 3.14
      def __init__ (self, radius):
            self.radius=radius
      def circumference (self):
            circum = 2 * self.pi * self.radius
            return circum
      def area (self):
            area = self.pi * self.radius**2
            return area

circle_1 = circle(4)
print(f"\nThe circumference of the circle is {circle_1.circumference()}")
print(f"\nThe area of the circle is {circle_1.area()}")



