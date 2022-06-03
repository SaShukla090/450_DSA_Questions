

def MoveArray(arr):
    N = len(arr)
    first_positive = None
    for i in range(N):
        if arr[i]>0 and first_positive == None:
            first_positive = i
        elif arr[i]<=0 and first_positive != None:
            arr[first_positive],arr[i] = arr[i], arr[first_positive]
            first_positive += 1
    return arr

if __name__ == "__main__":
    print("Enter the size of array\n")
    N = int(input())
    list1 = []
    print("Enter the Numbers\n")
    for i in range(N):
        ele = int(input())
        list1.append(ele)
	  
    print(list1,"/n")
    print("/n Hello World",MoveArray(list1))







