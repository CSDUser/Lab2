f1 = open("access.log",'r')
for line in f1.readlines():
	print(line)

mas1 = set()	
f1 = open("access.log",'r')	
import re	
for line in f1.readlines():	
	a = re.search( r'\d{0,3}[.]\d{0,3}[.]\d{0,3}[.]\d{0,3}', line)
	if a:
		mas1.add(a.group(0))
		
mas11 = mas1.copy()
leng = len(mas11)

myList=[]
for i in range(leng):
	myList.append(0)

i = 0
for line in mas11:
	myList[i] = line
	i=i+1

print('')	
myList.sort()
print('my_Sort_List:')
i = 0
for i in range(leng):
	print myList[i]

mas111 = set()	
c = 1
k = 0
t = 0 
for i in range(leng-1):	
	a = myList[i]
	b = myList[i+1]
	while c and t < 3:
		if a[k] == b[k]:			
			if a[k] == '.':
				t = t+1
			k = k+1
		else:
			c = 0
	if c:
		mas111.add(a)
		mas111.add(b)
	t = 0		
	k = 0
	c = 1
	
leng1 = len(mas111)

myList1=[]
for i in range(leng1):
	myList1.append(0)

i = 0
for line in mas111:
	myList1[i] = line
	i=i+1

myList1.sort()	

print('')	
print('Nonrecurring_IPs_of_the_same_roots:')	
d = 0
m = 1
for i in range(leng1-1):	
	a = myList1[i]
	b = myList1[i+1]
	while c and t < 3:
		if a[k] == b[k]:			
			if a[k] == '.':
				t = t+1
			k = k+1
		else:
			c = 0
			d = 0
	if c:
		if d == 0:
			print ('')
			print ("Subnetwork") 
			print (m)
			print(a)
			print(b)
			d = 1
			m = m+1
		else:
			print(b)

	t = 0		
	k = 0
	c = 1

