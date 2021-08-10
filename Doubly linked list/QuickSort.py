def partition(a,l,h) :
    x = a[h]
    i = l - 1
    for j in range(l,h) :
        if a[j] <= x :
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[h] = a[h],a[i+1]
    return i + 1

def quickSort(a,l,h) :
    if l < h :
        p = partition(a,l,h)
        quickSort(a,l,p-1)
        quickSort(a,p+1,h) 


li = [1,6,3,5,2]
quickSort(li,0,len(li)-1)
print(li)