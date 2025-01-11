def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True

        if swap == False:
            break

arr = [12, 1, 2, 3, 4, 8, 5, 11, 15, 14, 7, 6, 10, 9, 13]
BubbleSort(arr)

print("Sorted Array : ")
for i in range(len(arr)):
    print("%d" %arr[i],end=" ")