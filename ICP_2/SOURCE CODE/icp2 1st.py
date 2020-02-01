s = input("Please enter the number of students: ")
s = int(s)
lbs = []
kgs = []
for n in range(s):
        k = float(input("Enter the weight of student in lbs>>"))
        lbs.append(k)

kgs = [lbs[x] * 0.453592 for x in range(s)]

print(kgs)