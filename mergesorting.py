def mergesort(A,left,right):
    if right - left <= 1:
        return(A[left:right])
    if right - left > 1:
        mid = (left+right)//2
        L = mergesort(A,left,mid)
        R = mergesort(A,mid,right)
        return(merge(L,R))    
def merge(a,b):
    (c,m,n) = ([],len(a),len(b))
    (i,j) = (0,0)
    while i+j <m+n:
        if i == m:
            c.append(b[j])
            j = j+1
        elif j == n:
            c.append(a[i])
            i = i+1
        elif a[i]<b[j]:
            c.append(a[i])
            i = i+1
        elif b[j]<a[i]:
            c.append(b[j])
            j = j+1
    return(c)