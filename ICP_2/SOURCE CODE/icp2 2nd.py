
def string_alternative(str1, n, b=""):
    for i in range(n):
        if i % 2 == 0: #taking alternative charectors
         b +=str1[i] #appending into new string
    print(b)

stre=input("enter string") #taking values
n=len(stre); #calculating the length
string_alternative(stre,n) #calling the function

#input= h h sjdfn
#output=hh jf