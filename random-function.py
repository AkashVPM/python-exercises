# WAP which one is going to pay the bill for food amoung our friends

import random

friends_name = input("enter the name of the friends with camma: ")
friends_name_list1 = friends_name.split(",")
sponcer = random.choice(friends_name_list1)
print(friends_name)
print(sponcer)