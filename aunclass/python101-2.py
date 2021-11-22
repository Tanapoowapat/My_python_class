"""
a = 10
b = 5

print(a > b)

if a > b : 
    print("A is bigger than B")
else : 
    print("A is not bigger than B")

height = int(input("Enter Height : "))

if height < 120:
    print("Free pass!")
else:
    print("Pay 60 Baht to pass")

num = int(input("Enter Number : "))
if num % 2 == 0:
    print(str(num) + " is even number")
elif num % 2 != 0:
    print(str(num) + " is odd number")


num = int(input("Enter your speed : "))

if(num > 90) :
    print("Hight speed!")
elif(num < 90 and num >= 45):
    print("Medium speed")
else:
    print("Slow speed")
grade = int(input("Enter your score : "))
if(grade < 50):
    print("F")
elif grade >= 50 and grade <= 59 :
    print("D")
elif grade >= 60 and grade <= 69 :
    print("C")
elif grade >= 70 and grade <= 79 :
    print("B")
elif grade >= 80 and grade <= 100:
    print("A")
else :
    print("WTF!?")

id_card = input("Do you bring your ID card with? : ").upper()
if(id_card == 'Y'):
    birthyear = int(input("What year do you born? : "))
    if((2021 - birthyear) >= 18):
        print("Welcome to pub!")
    else:
        print("Sorry you're under 18")
elif(id_card == 'N') :
    print("Please bring your ID card with you next time!")
else:
    print("Error!")

mylist = ["Books", "Cars", "20 Girlfriend in Germany"]

print(mylist[0:2:])

car_brand_1 = ["Toyota","BMW","Suzuki"]
car_brand_2 = ["Tesla","Ferrari","Porsche"]

car_brand_1.extend(car_brand_2)
car_brand_1.append("Benz")
car_brand_1.insert(4,"Tesla China version")
car_brand_1 += "Tank" # ใช้เฉพาะสำหรับเช็คตัวอักษร ไม่นิยมใช้
print(car_brand_1)

car_brand_1 = ["Toyota","BMW","Suzuki"]
car_brand_2 = ["Tesla","Ferrari","Porsche"]

car_brand_1.extend(car_brand_2)
#car_brand_1.remove("Suzuki")
#del car_brand_1[2]
#car_brand_1.pop(2)

car_brand_1.clear()
print(car_brand_1)
    

number_list = [102, 66, 98, 12, 5, 79, 50]

number_list.sort(reverse=True)
print(number_list)"""

car_brand_1 = ["Toyota","BMW","Suzuki"]
car_brand_2 = ["Tesla","Ferrari","Porsche"]

car_brand_1.extend(car_brand_2)

Mydream = car_brand_1.copy()
print(*Mydream, sep= ", ", end= ".")