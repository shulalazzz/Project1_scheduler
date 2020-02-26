arr = [[]] * 3

arr[0].append(10)

print("length: " + str(len(arr)))
print("length: " + str(len(arr[0])))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])

print()
arr[1][0] = 20
print(arr[1][0])
print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])

print()
arr[0][0] = 5
print(arr[0][0])
print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])
