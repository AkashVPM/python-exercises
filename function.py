import statistics
def number(list):
      return statistics.mean(list), statistics.mode(list), statistics.median(list)

a,b,c = number([2,5,7,6,5,2,8,6,3])
print("the mean is ", a)
print("the mode is ", b)
print("the median is ", c)