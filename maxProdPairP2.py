#python3

n = int(input())
num = input().split()

max1 = -1

for i in range(n):
	if max1 == -1 or int(num[max1]) < int(num[i]):
		max1 = i

max2 = -1

for j in range(n):	
	if (max2 == -1 and max1 != j) or ( int(num[max2]) < int(num[j]) and j != max1) :
		max2=j

		
print(int(num[max1])*int(num[max2]))