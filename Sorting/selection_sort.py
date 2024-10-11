def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]

def show(arr):
    for var in arr:
        print(var,end=" ")
    print()

if __name__=="__main__":
    arr = [23,33,12,46,11]

    print("Original array: ",end="")
    show(arr)
    
    selection_sort(arr)

    print("Sorted array: ",end="")
    show(arr)