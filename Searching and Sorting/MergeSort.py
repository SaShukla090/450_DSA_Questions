def MergeSort(arr, s, e):
    print("\ns = ", s, "e = ", e)
    if (s>=e) or (e - s)==1:
        return
    elif e - s == 2:
        if arr[s]>arr[s+1]:
            arr[s], arr[s+1] = arr[s+1], arr[s]
        else:
            return
    else:
        mid = (e - s)//2 + s
        MergeSort(arr, s, mid)
        MergeSort(arr, mid, e)
        Merge(arr,s, mid, e)


def Merge(arr, s, mid, e):
    m = mid - s - 1
    n = e - mid - 1
    i = 0
    j = 0
    k = 0
    A = []
    while(m>i and n>j):
        if arr[s + i] > arr[mid + j]:
            A.append(arr[mid + j])
            j += 1
            k +=1
        else:
            A.append(arr[s + i])
            i += 1
            k += 1
    if i<=m:
        for h in range(i,m):
            A.append(arr[h])
            i +=1
            k += 1
    elif j<=n:
        for b in range(j,n):
            A.append(b)
            j += 1
            k += 1
    for i in range(m+n):
        arr[s+i] = A[i]





arr = [7,5,6,4,8,3,9]
MergeSort(arr, 0, len(arr))

print(arr)







