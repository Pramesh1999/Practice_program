#reverse the string without reversing its individual words. Words are separated by dots.
def reverseWords(S):
     #first split the string into dots
    word = S.split(".")
   #then reverse the split stringlist and join using dots
    reverse_word ='.'.join(reversed(word))
    #finally return the joined stringlist
    return reverse_word
           
#Drive code
if __name__ == "__main__":
    s = str(input())
    print(reverseWords(s))
     
      
 #OUT PUT
"""
I.like.this.program.very.much                                                                                                            
much.very.program.this.like.I     
"""
