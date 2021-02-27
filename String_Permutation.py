#write the program string permutation
#duplicated allowed
def tostring(List):
    return ''.join(List)
def permutation(a,l,r):
    if(l == r):
        print(tostring(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permutation(a,l+1,r)
            a[l],a[i] = a[i],a[l]

string = input("enter string")
a = list(string)
n = len(a)
permutation(a,0,n-1)


#OUT PUT
"""
enter stringABC                                                                                                                            
ABC                                                                                                                                        
ACB                                                                                                                                        
BAC                                                                                                                                        
BCA                                                                                                                                        
CBA                                                                                                                                        
CAB                                                                                                                                        
 """
