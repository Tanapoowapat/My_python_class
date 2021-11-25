#------------------------------
# tuple just like list
#------------------------------
mytuple = ('red','green','blue')
std_info = (1,'Tanapoowapat','Yomsarn')


#------------------------------
# tuple cant update value or delete value inside of it
# to update or delete we must covert tuple to list then covert back to tuple again
#------------------------------

std_info = (1,'Tanapoowapat','Yomsarn')
print(std_info)
X = list(std_info)
X[0] = "64015060"
std_info = tuple(X)
print(std_info)

#--------------------------------
# For loop      #
# while loop    #
#--------------------------------

while True:


i = 1
while i < 10:
    print(i)
    i += 1

#--------------------------------
i = 0
while i < 11:
    print(i)
    if i == 7:
        break
    i+=1

#--------------------------------
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#---------------------------------
# For loop 
#----------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#---------------------------------


#---------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#---------------------------------
# Range fucntion
#---------------------------------


for x in range(6):
  print(x)


#---------------------------------
for x in range(2, 6):
  print(x)

#---------------------------------
muti = int(input('multiplication table : ')) 
for i in range(1,13):
    result  = muti *  i
    print(f'{muti} * {i} = {result}')



#---------------------------------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#--------------------------------
s = "Nobody can predict the future, only a firm grasp on the present."
c = 0
for e in s :
    if e in['a','e','i','o','u']:
        c += 1
print(f"String has vowel {c} charecters.")

#---------------------------------
#-------------------------------------------
#* ในการวน loop บางครั้งเราต้องการให้ข้ามไป
#* จะใช้ pass ดังตัวอย่าง
#-------------------------------------------

for letter in 'Python':
    if letter == 'h':
        pass
        #print ("This is pass block")
    else:
        print ("Current Letter :", letter)

#-------------------------------------------
#* การออกจาก Loop จะใช้ break
#-------------------------------------------

for i in range(5):
    for j in range(6):
        print(f'j={j}')
        if (j==4):      # condition 1
            break       # break นี้ออกจาก for j
    print(f'i={i}')
    if (i==2) :         # condition 2
        break           # break นี้ออกจาก for i
#------------------------------------------


#* List Comprehension
#* โครงสร้างจะมี 2 ส่วน คือ หน้า for กับหลัง for
#* ส่วนหลัง for จะเป็นคำสั่ง for ตามปกติ
#* ส่วนหน้า for จะเป็นคำสั่งที่ execute ตาม loop ได้คำสั่งเดียวหรือ fn
#* ผลลัพธ์ที่ได้จะอยู่ใน list

even = [num for num in range()]

squares = [value**2 for value in range(1,11) if value % 3 == 0]
print(squares)