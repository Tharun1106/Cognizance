# Q5.Print the following pattern.
l = int(input("Enter the number of rows:"))
m = (2*l)-2
for i in range(0, l):
		for j in range(0, m):
			print(end=" ")
		m = m - 1
		for j in range(0, i + 1):
			print("* ", end='')
		print("")