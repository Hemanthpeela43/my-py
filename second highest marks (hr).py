n=int(input())
res=[]
grade=[]
for i in range (n):
    name=input()
    marks=float(input())
    res.append([name,marks])
    grade.append(marks)
grade=sorted(set(grade))
m=grade[1]
name=[]
for val in res:
    #we have name and marks in value so val[1] is to take marks by indexing
    if m==val[1]:
        name.append(val[0])
name.sort()
for nm in name:
    print(nm)
