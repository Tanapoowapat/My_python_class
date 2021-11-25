#tuple
"""
mylist = ("Rat", "Bat", "Man")
print(mylist)

n = list(mylist)
n[0] = "This is "
mylist = tuple(n)
print(mylist)

#while loop
i = 0
while True:
    print(i)
    if i >= 21:
        break
    i += 1

#short while
i = 0
while i < 6:
    i +=1
    if i == 3: #not count 3
        continue
    print(i)

#for loop
names = ["App", "Car", "EIEI"]

for i in names:
    print(i)
    if i == "Car":
        break

for i in range(0, 20, 2):
    print(i)

multi = int(input("Enter number : "))

for i in range(1, 13):
    result = multi * i
    print(f"{multi} * {i} = {result}")
"""

arr1 = ["red", "green", "blue"]
arr2 = ["yello", "black", "white"]

for i in arr1:
    for j in arr2:
        print(i, j)


text = "HELLO HOW ARE YOU TODAY? I'M FINE THANKS AND YOU? I'M GOOD THANKS"
count = 0
for i in text.lower():
    if i in["a", "e", "i", "o", "u"]:
        count += 1
print(f"Total {count} characters")


for letter in "Python":
    if letter == "h":
        pass
    else:
        print(letter)

for i in range(5):
    for j in range(6):
        print(f"j={j}")
        if(j==4):
            break
    print(f"i={i}")
    if(i==2):
        break

mylist = []

for num in range(1, 20+1):
    if(num % 2 == 0):
        mylist.append(num)
print(mylist)

prime = [num for num in range(0, 20+1) if num % 2 == 1]
print(prime)