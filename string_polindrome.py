#longestpolindrome in string

def longestpolindrome(string):
    maxlength = 1 
    length = len(string)
    low = 0
    high = 0
    start = 0
    for i in range(length):
        low = i-1
        high = i
        while(low>=0 and high<length and string[low] == string[high]):
            if(high-low+1>maxlength):
                start = low
                maxlength  = high-low+1 
            low = low-1
            high = high+1 
        low = i-1
        high = i + 1 
        while(low>=0 and high<length and string[low] == string[high]):
            if(high-low+1>maxlength):
                start = low
                maxlength = high-low+1 
            low -= 1 
            high += 1 
    print(string[start : start+maxlength])
num = int(input())
list1 = []
for i in range(num):
    string1 = input()
    list1.append(string1)
for string in list1:
    longestpolindrome(string)

