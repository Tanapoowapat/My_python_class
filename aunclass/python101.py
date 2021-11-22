"""
print ("Hi!")
print ('printtest')

print("*"*10)

print("Hello"+"Thailand!")


^ ใช้หลายบรรทัด
 ############## - ใช้บรรทัดเดียว
"""

name = "Aun"
age = 19
weight = 65.2
man = True

#เปลี่ยนค่าตัวแปลจาก int เป็น string
"""print(type(str(age)))

name_1 = input("Enter Name : ")
print(name_1)

age = int(input("Enter age : "))
print(age)
"""

"""print(1+1)
print(2-1)
print(9*1)
print(10/2)
print(2**6)
print(80//2)
print(10%3) """

#side1 = int(input("Enter ด้านที่1 : ")) #หรือ side = int(input("Enter side : "))

#side2 = int(input("Enter  ด้านที่ 2 :")) 

#sum = side1 * side2 # side *= side
#print(sum)

### FORMAT ###

name = "Prachar"
age = 21

print(f"Name : {name} \nAge : {age}") #!important

num1, num2 = input("Enter Number : ").split()
print(num1, num2)

# Loop in input
num3, num4 = [int(e) for e in input().split()]
print (num3, num4)

a = 'n'
b = 'u'
c = 't'
print(a, b, c, sep="000000", end=' Bye!') 

#slice string
slicename = "Watthachai"
print(slicename[0:4:2]) #start 0 stop 4 [start:stop:step]
print(slicename[-1]) #last char
print(slicename[:4:]) #skip index char to 4