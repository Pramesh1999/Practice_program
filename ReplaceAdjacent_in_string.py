def recursively(st):
    list1 = []
    i = 0
    while(i<len(st)):
        if(i<len(st)-1 and st[i]!=st[i+1]):
            list1.append(st[i])
            i += 1 
        if(i<len(st)-1 and st[i] == st[i+1]):
            while(i<len(st)-1 and st[i]==st[i+1]):
                i +=1 
            i +=1 
    for x in list1:
        print(x,end="")
    print()
num = int(input())
list2 = []
for i in range(num):
    a = input()
    list2.append(a)
for i in list2:
    recursively(i)
