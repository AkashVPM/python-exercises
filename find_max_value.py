number = list(str(input("enter the velue: ")))
number.sort()
a=max(number)
sec_number = number[::1]
# print(sec_number)
list=[]
for i in sec_number:
      if i not in list:
            list.append(i)

list.remove(a)
print(number)
print(max(list))