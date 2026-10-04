num = int(input("enter the number:"))
if num % 2 != 0:
    print("Weird")
elif num % 2 == 0 and (2<num<5):
    print("Not Weird")
elif num % 2 == 0 and (6<num<20):
    print("Weird")
elif num % 2 == 0 and (20<num):
    print("Not Weird")