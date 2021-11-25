#-------------------------------------------
# compare operator
# == เท่ากับ
# != ไม่เท่ากับ
# >  น้อยกว่า
# <  มากกว่า
# >= มากกว่าเท่ากับ 
# <= น้อยกว่าเท่ากับ
#-------------------------------------------

a = 10
b = 5

if a > b : print("A bigger then B")

#-------------------------------------------
#if condition : 
#   statment 
#-------------------------------------------

height = int(input("Enter Hieght : "))
if height > 120:
    print("Free pass!")
else:
    print("Pay 60 Bath to pass")

#-------------------------------------------

num = int(input("Enter Number : "))
if num % 2 == 0 :
    print(num + "is even number ")
elif num % 2 != 0:
    print(f"{num} is odd number ")

#-------------------------------------------#
#   เขียนโปรแกรม วัดความเร็ว
#   ถ้าความเร็วมากกว่า 90 ให้แสดงผลเป็น Hight speed ! 
#   ถ้าความเร็วระหว่าง 45->90 ให้แสดงผลเป็น medium speed ! 
#   ถ้าความเร็วต่ำกว่า 45 ให้แสดงผลเป็น slow speed ! 
#-------------------------------------------#
#   &&  ||  !=
#   and or not
#   if speed > 90 and speed < 45 :


# nest if
#-------------------------------------------#
grade = int(input("Enter you grade : "))
if grade < 50 :
    print("F")
elif grade >= 50 and grade < 55 :
    print("D")
elif grade >= 55 and grade < 60 :
    print("D+")
elif grade >= 60 and grade < 65:
    print("C")
elif grade >= 65 and grade < 70:
    print("C+")
elif grade >= 70 and grade < 75:
    print("B")
elif grade >= 75 and grade < 80:
    print("B+")
elif grade >= 80:
    print("A")
elif grade > 100:
    print("Error Score over 100 !")



#-------------------------------------------#


id_card = input("Have id card [Y:N] ? :").lower()

if id_card == 'Y' or id_card == 'y':
    age = int(input("Enter your age : "))
    if age >= 18 :
        print("Welcome to pub!")
    else:
        print('Sorry you are under 18')
else:
    print("Pls bring id card with you next time !")




#-------------------------------------------#

# -------------------------------------------------------------------------
# list เป็นโครงสร้างฐานข้อมูล คล้ายกับ Array เเต่ว่าสามารถชนิดข้อมูลต่างกันได้
# -------------------------------------------------------------------------

mylist = ["Apple","Orange","Watermelon"]
student_list = [64015060,"Tanapoowapat Yomsarn","21","Lampang"]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# -------------------------------------------------------------------------

# การอ้างถึงข้อมูลใน list ต้องอ้างเป็นตำแหน่งใน list เริ่มต้นจาก 0 
# การอ้างถึงคล้ายกับ string ใช้วิธีเดียวกันได้ทั้งหมด

# -------------------------------------------------------------------------

print(num_list[0])
print(num_list[2])
print(num_list[0::2])
print(num_list[1:7])

print(f'Richard like {mylist[0]}')
print(f'Tom like {mylist[1]}')
print(f'Jerry like {mylist[2]}')

# -------------------------------------------------------------------------

# วิธีเพิ่มข้อมูลลงใน list จะมีคำสั่ง extend, append, insert, +
# extend จะเพิ่ม List เข้าไป List mylist1.extend(mylist2)
# append จะเพิ่มข้อมูลเข้า list ในตำแหน่งสุดท้าย mylist.append("Rose")
# insert จะเพิ่มข้อมูลเข้า list โดยอ้างอิงจากตำแหน่ง mylist.insert(0, "Jackson")
# -------------------------------------------------------------------------

car_brand_1 = ["Toyota","BMW","Suzuki"]
car_brand_2 = ["Tesla","Ferrari","Porsche"]

car_brand_1.append("Ford")
car_brand_1.insert(0,"Audi")
car_brand_1.extend(car_brand_2)
car_brand_1 += 'Subaru'

# -------------------------------------------------------------------------
# ลบข้อมูลใน List จะมีคำสั่ง pop, remove, del, clear
# clear ลบข้อมูลใน list ทั้งหมด
# remove ลบข้อมูลใน list โดยการอ้างอิงชื่อ
# del ลบข้อมูลใน list โดยอ้างอิงตำแหน่ง
# pop ลบข้อมูลใน list  หากไม่อ้างอิงตำแหน่งจะทำการลบข้อมูลในตำแหน่งสุดท้าย
# -------------------------------------------------------------------------

mylist1 = ['Apple','Orange', 'Pineapple','Melon','Water melon','banana']

mylist1.remove('Melon')
del mylist1 [1]
mylist1.pop()
mylist1.pop(4)
mylist.clear()

# -------------------------------------------------------------------------
# Sort in list
# -------------------------------------------------------------------------

this_list = [120,55,90,12,25]
that_list = [99,98,88,200,1000]

this_list.sort()
that_list.sort( reverse= True)

# -------------------------------------------------------------------------

my_list1 = ["apple", "banana", "cherry"]
my_list2 = ["Water melon", "Melon", "stawberry"]

my_list2.copy(my_list1)

# -------------------------------------------------------------------------
