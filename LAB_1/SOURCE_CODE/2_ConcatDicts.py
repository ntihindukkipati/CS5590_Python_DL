dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
dict2 = {'bookD': 6, 'bookE': 4, 'bookF': 5}

#Merging two dictionaries
dict2.update(dict1)
print(dict2)

#sorting the merged dictionaries and printing the values
for v,k in sorted(dict2.items(), key=lambda x: x[1]):
    print (v,':',k)