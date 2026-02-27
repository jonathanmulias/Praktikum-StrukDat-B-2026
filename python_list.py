#PYTHON LIST
#|| PYTHON LIST ||

print("-------------------------------------------------------------------------------------------------")

print("PYTHON LIST")

nama = ["Riva", "Rahmania", "Ketrin"]
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Kahijina", "Gama"]
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Kahijina', 'Gama']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
print(len(nama))

#Outputnya :
#3

print("-------------------------------------------------------------------------------------------------")

nama1 = ["Riva", "Rahmania", "Ketrin"]
nama2 = [18, 18, 19]
nama3 = [True, False, False]

print(nama1)
print(nama2)
print(nama3)

#outputnya :
#['Riva', 'Rahmania', 'Ketrin']
#[18, 18, 19]
#[True, False, False]

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", 18, True, 167, "perempuan"]

print(nama)

#Outputnya :
#['Riva', 18, True, 167, 'perempuan']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
print(type(nama))

#Outputnya :
#<class 'list'>

print("-------------------------------------------------------------------------------------------------")

nama = list(("Riva", "Rahmania", "Ketrin"))
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

#|| ACCESS LIST ITEMS ||

print("ACCESS LIST ITEMS")

nama = ["Riva", "Rahmania", "Ketrin"]
print(nama[-1])

#Outputnya :
#Ketrin

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Kahijina", "Gama"]
print(nama[2:5])

#Outputnya :
#['Ketrin', 'Kahijina', 'Gama']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Kahijina", "Gama"]
print(nama[:4])

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Kahijina']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Kahijina", "Gama"]
print(nama[2:])

#Outputnya :
#['Ketrin', 'Kahijina', 'Gama']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Kahijina", "Gama"]
print(nama[-4:-1])

#Outputnya : 
#['Rahmania', 'Ketrin', 'Kahijina']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
if "Ketrin" in nama:
  print("Ketrin ada di dalam list")

#Outputnya :
#Ketrin ada di dalam list

print("-------------------------------------------------------------------------------------------------")

#|| CHANGE LIST ITEMS || 

print("CHANGE LIST ITEMS")

nama = ["Riva", "Rahmania", "Ketrin"]
nama[1] = "Riva"
print(nama)

#Outputnya :
#['Riva', 'Riva', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Kahijina", "Gama"]
nama[1:3] = ["Damar", "Erza"]
print(nama)

#Outputnya :
#['Riva', 'Damar', 'Erza', 'Kahijina', 'Gama']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama[1:2] = ["Damar", "Erza"]
print(nama)

#Outputnya :
#['Riva', 'Damar', 'Erza', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama[1:3] = ["Carlos"]
print(nama)

#Outputnya :
#['Riva', 'Carlos']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.insert(2, "Carlos")
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Carlos', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

#|| ADD LIST ITEMS || 

print("ADD LIST ITEMS")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.append("Kahijina")
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Kahijina']

print("-------------------------------------------------------------------------------------------------")

nama1 = ["Riva", "Rahmania", "Ketrin"]
nama2 = ["Kahijina", "Gama", "Carlos"]
nama1.extend(nama2)
print(nama1)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Kahijina', 'Gama', 'Carlos']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
makanan = ("Batagor", "Bakso")
nama.extend(makanan)
print(nama)

#Contohnya :
#['Riva', 'Rahmania', 'Ketrin', 'Batagor', 'Bakso']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.insert(1, "Damar")
print(nama)

#Contohnya :
#['Riva', 'Damar', 'Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

#|| REMOVE LIST ITEMS || 

print("REMOVE LIST ITEMS")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.remove("Ketrin")
print(nama)

#Contohnya :
#['Riva', 'Rahmania']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]
nama.remove("Damar")
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Karlos']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.pop(1)
print(nama)

#Outputnya :
#['Riva', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.pop()
print(nama)

#Outputnya :
#['Riva', 'Rahmania']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
del nama[0]
print(nama)

#Outputnya :
#['Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
nama.clear()
print(nama)

#Outputnya :
#[]

print("-------------------------------------------------------------------------------------------------")

#|| LOOP LISTS || 

print("LOOP LISTS")

nama = ["Riva", "Rahmania", "Ketrin"]
for x in nama:
  print(x)

#Outputnya :
#Riva
#Rahmania
#Ketrin

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
for i in range(len(nama)):
  print(nama[i])

#Outputnya :
#Riva
#Rahmania
#Ketrin

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
i = 0
while i < len(nama):
  print(nama[i])
  i = i + 1

#Outputnya :
#Riva
#Rahmania
#Ketrin

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
[print(x) for x in nama]

#Outputnya :
#Riva
#Rahmania
#Ketrin

print("-------------------------------------------------------------------------------------------------")

#|| LIST COMPREHENSION || 

print("LIST COMPREHENSION")

nama1 = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]
nama2 = []

for x in nama1:
  if "a" in x:
    nama2.append(x)

print(nama2)

#Outputnya :
#['Riva', 'Rahmania', 'Damar', 'Karlos']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]

namabaru = [x for x in nama if "a" in x]

print(namabaru)

#Outputnya :
#['Riva', 'Rahmania', 'Damar', 'Karlos']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]

namabaru = [x for x in nama if x != "Rahmania"]

print(namabaru)

#Outputnya :
#['Riva', 'Ketrin', 'Damar', 'Karlos']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]

namabaru = [x for x in nama]

print(namabaru)

#Outputnya 
#['Riva', 'Rahmania', 'Ketrin', 'Damar', 'Karlos']

print("-------------------------------------------------------------------------------------------------")

listbaru = [x for x in range(20)]

print(listbaru)

#Outputnya :
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print("-------------------------------------------------------------------------------------------------")

listbaru = [x for x in range(20) if x < 10]

print(listbaru)

#Outputnya :
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]

namabaru = [x.upper() for x in nama]

print(namabaru)

#Outputnya :
#['RIVA', 'RAHMANIA', 'KETRIN', 'DAMAR', 'KARLOS']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]

namabaru = ['hello' for x in nama]

print(namabaru)

#Outputnya :
#['hello', 'hello', 'hello', 'hello', 'hello']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]

namabaru = [x if x != "Ketrin" else "Karlos" for x in nama]

print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Damar', 'Karlos']

print("-------------------------------------------------------------------------------------------------")

#|| SORT LISTS || 

print("SORT LISTS")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]
nama.sort()
print(nama)

#Outputnya :
#['Damar', 'Karlos', 'Ketrin', 'Rahmania', 'Riva']

print("-------------------------------------------------------------------------------------------------")

nilai = [100, 90, 80, 70, 60]
nilai.sort()
print(nilai)

#Outputnya :
#[60, 70, 80, 90, 100]

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]
nama.sort(reverse = True)
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin', 'Karlos', 'Damar']

print("-------------------------------------------------------------------------------------------------")

nilai = [100, 90, 80, 70, 60]
nilai.sort(reverse = True)
print(nilai)

#Outputnya :
#[100, 90, 80, 70, 60]

print("-------------------------------------------------------------------------------------------------")

def data(n):
  return abs(n - 60)

nilai = [100, 90, 80, 70, 60]
nilai.sort(key = data)
print(nilai)

#Outputnya :
#[60, 70, 80, 90, 100]

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]
nama.sort()
print(nama)

#Outputnya :
#['Damar', 'Karlos', 'Ketrin', 'Rahmania', 'Riva']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin", "Damar", "Karlos"]
nama.sort(key = str.lower)
print(nama)

#Outputnya :
#['Damar', 'Karlos', 'Ketrin', 'Rahmania', 'Riva']

print("-------------------------------------------------------------------------------------------------")

#|| COPY LISTS || 

print("COPY LISTS")

nama = ["Riva", "Rahmania", "Ketrin"]
datanama = nama.copy()
print(datanama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
datanama = list(nama)
print(nama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

nama = ["Riva", "Rahmania", "Ketrin"]
datanama = nama[:]
print(datanama)

#Outputnya :
#['Riva', 'Rahmania', 'Ketrin']

print("-------------------------------------------------------------------------------------------------")

#|| JOIN LIST || 

print("JOIN LIST")

data1 = ["P", "Q", "R"]
data2 = [4, 5, 6]

data3 = data1 + data2
print(data3)

#Outputnya :
#['P', 'Q', 'R', 4, 5, 6]

print("-------------------------------------------------------------------------------------------------")

data1 = ["P", "Q", "R"]
data2 = [4, 5, 6]

for x in data2:
  data1.append(x)

print(data1)

#Outputnya :
#['P', 'Q', 'R', 4, 5, 6]

print("-------------------------------------------------------------------------------------------------")

data1 = ["P", "Q", "R"]
data2 = [4, 5, 6]

data1.extend(data2)
print(data1)

#Outputnya 
#['P', 'Q', 'R', 4, 5, 6]

print("-------------------------------------------------------------------------------------------------")

