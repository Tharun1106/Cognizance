#Q3.Write a python program to make a 2-dimensional list that contains
#represents a table of records, for instance, student details like Roll no,
#Student Name, Marks; And complete the following 2 sub-tasks.
# i) Add some records in the list and print the list in tabular form,
# ii) From created list, extract and print second record/row that contains,
print('i')
V=['Roll No    Student Name    Marks',
   '   1         Tharun         100 ',
   '   2         Sidesh         90  ',
   '   3         Madhan         95  ']
for i in range(4):
    print(V[i])
print()
print('ii')
n=int(input("Enter roll number:"))
a=1
b=2
c=3
if n==a:
    print(V[1])
elif n==b:
    print(V[2])
elif n==c:
    print(V[3])
else:
    print("Enter proper roll number: ")