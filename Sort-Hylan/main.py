import random
#tohle je bubblesort
array = [random.randint(0, 100) for _ in range(10)]
print("původní pole 1:", array)
for i in range(len(array)):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print("seřazené pole 1(babl):", array)
#tohle je bogosort
arraya = [random.randint(0, 100) for _ in range(5)]
print("původní pole 2:", arraya)
while arraya != sorted(arraya):
    random.shuffle(arraya)
print("seřazené pole(bogo):", arraya)
#tohle je selection sort
arrayb = [random.randint(0, 100) for _ in range(10)]
print("původní pole 3:", arrayb)

for i in range(len(arrayb)):
    for j in range(i + 1, len(arrayb)):
        if arrayb[j] < arrayb[i]:
            arrayb[i], arrayb[j] = arrayb[j], arrayb[i]

print("seřazené pole 3 (selection):", arrayb)

#tohle je insert sort
arrayc = [random.randint(0, 100) for _ in range(10)]
print("původní pole 4:", arrayc)
for i in range(1, len(arrayc)):
    key = arrayc[i]
    j = i - 1
    while j >= 0 and key < arrayc[j]:
        arrayc[j + 1] = arrayc[j]
        j -= 1
    arrayc[j + 1] = key
print("seřazené pole 4 (insert):", arrayc)
