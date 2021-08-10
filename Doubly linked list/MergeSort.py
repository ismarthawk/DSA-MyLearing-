def merge(a,l,h,mid) :
    lt = a[l:mid+1] + [float('inf')]
    rt = a[mid+1:h+1] + [float('inf')]
    pos = l
    j = i = 0
    while pos <= h :
        if lt[i] <= rt[j] :
            a[pos] = lt[i]
            i += 1
        else :
            a[pos] = rt[j]
            j += 1
        pos += 1
def mergeSort(a,l,h) :
    if l < h :
        mid = (l+h) // 2
        mergeSort(a,l,mid)
        mergeSort(a,mid+1,h)
        merge(a,l,h,mid)

a = [1,5,3,2,6]
mergeSort(a,0,len(a)-1)
print(a)
    
