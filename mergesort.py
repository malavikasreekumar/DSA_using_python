def mesort(A):
    l=len(A)
    left=l//2
    right=l
    
    def mergesort(A,left,right):
        if right-left<=1:
            return(A[left:right])
        if right-left>1:
            mid=(left+right)//2
            L=mergesort(A,left,mid)
            R=mergesort(A,mid,right)
            
            return(merge(L,R))
   


    def merge(D,B):
        (C,m,n)=([],len(D),len(B))
        (i,j)=(0,0)
        #C=[1,23,7]
        while i+j<m+n:
            if i==m:
                C.append(B[j])
                j=j+1
            elif j==n:
                C.append(D[i])
                i=i+1
            elif D[i]<=B[j]:
                C.append(D[i])
                i=i+1
            elif D[i]>B[j]:
                C.append(B[j])
                j=j+1
        print(C)
        return(C)
        
           
        
        
    
   
X=[34,56,12,89,11,9,45]
mesort(X)
    