from itertools import combinations
n = int(input("Enter the size of an array for which you want all the subsets: >>"))
print ("Enter all the values:")
full_set = []
#Inputs all the values and inserting into an array
for i in range(0, n):
    ele = int(input())
    full_set.append(ele)
#Running a loop and finding out all the combinations
for i in range(1,n+1):
    print(list(combinations(full_set, i)))



