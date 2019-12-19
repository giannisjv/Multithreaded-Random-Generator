#!/usr/bin/env python
import time
import random as ra
import pyautogui
from threading import Thread 

start_time = time.time()
A=[]    								#Αρχικοποίηση λιστων για τις συντεταγμένες και τις τιμες του RGB A = x B = y
B=[]
Red=[]
Green=[]
Blue=[]

print("**********************************************************************************")
print("* The Random Generator Will run with 10 threads for almost 20 secs, gathering info")
print("* Including mouse position and RGB values from your screen.")
print("* Then it will give you the Number out of your entropy") 
print("* Threads can run parallel to each other so it won't take any longer.")
print("* For Better results feel free to use your Computer")
print("**********************************************************************************")

def myfunc(i):
	ran = ra.randrange(20) 						#Τυχαία επιλογή των δευτερολέπτων που θα τρέξει το κάθε Thread
	#print("thread: %d will sleep for seconds %d , \n When it will wake up it will pick the mouse location in random time! "%(i,ran))
	time.sleep(ran)								#Κοίμησε το Τhread για ran δευτερόλεπτα
	
	x,y = pyautogui.position()					#Αποθήκευση συντεταγμένων της οθόνης.
	r,g,bl = pyautogui.pixel(x,y)				#Αποθήκευση των τιμών RGB των Pixel από τις συντεταγμένες τις οθόνης.
	
	#print("awaken %d with values x=: %d and y: %d\n"%(i,x,y))
	
	A.append(x)									#Αποθήκευσε την τιμή του x στην λιστα Α
	B.append(y)									#Αποθήκευσε την τιμή του y στην λιστα B
	Red.append(r)								#Αποθήκευσε την τιμή του r στην λιστα Red
	Green.append(g)								#Αποθήκευσε την τιμή του g στην λιστα Green
	Blue.append(bl)								#Αποθήκευσε την τιμή του b στην λιστα Blue
	


for i in range(10):								#Από 0 εως 9 
	t=Thread(target=myfunc, args=(i,))			#Με στόχο το myfunc φτίαξε i threads
	t.start()

for i in range(0, len(A)):						#Μετατροπή της Λιστας σε integer!
	A[i] = int(A[i])
	
for i in range(0, len(B)):
	B[i] = int(B[i])
	
for i in range(0, len(Red)):
	Red[i] = int(Red[i])
	 
for i in range(0, len(Green)):
	Green[i] = int(Green[i])
	
for i in range(0, len(Blue)):
	Blue[i] = int(Blue[i])
	
	
time.sleep(20)									#Κοιμήσου για 20 δευτερόλεπτα περιμένοντας τα Threads να τελειώσουν
RandomNumber= (A + B + Red + Blue +Green)		#πρόσθεσε όλες τις λίστες σε μία
Sum=sum(RandomNumber)							#πρόσθεσε τα δεδομένα όλων των λιστών σε ενα ιnt
SumA = sum(A)										#πρόσθεσε τα δεδομένα της λίστας Α σε ενα ιnt
SumB=sum(B)
SumRed=sum(Red)
SumGreen=sum(Green)
SumBlue=sum(Blue)



#print(*A+B+Red+Blue+Green, sep = " ")
pick = ra.randrange(5)
	
if pick == 0:
	Random_number = ((Sum*SumA)-2)/10000			#Υπολογισμός του Random Number!
elif pick == 1:
	Random_number = ((Sum*SumB)-2)/10000
elif pick == 2:
	Random_number = ((Sum*SumRed)-2)/10000
elif pick == 3:
	Random_number = ((Sum*SumGreen)-2)/10000
elif pick == 4:
	Random_number = ((Sum*SumBlue)-2)/10000
		
end_time = time.time()

time_value = end_time - start_time


print("\n")
print("**********************************************************************************")
print("\t\t\tΤιμές Λιστών")
print("\n* Τιμές χ",*A, sep =  ", ")
print("\n* Τιμές y",*B, sep = ", ")
print("\n* Τιμές Red",*Red, sep = ", ")
print("\n* Τιμες Green",*Green, sep = ", ")
print("\n* Τιμες Βlue",*Blue,sep = ", ")
print("**********************************************************************************")
print("\n")	
print("**********************************************************************************")
print("\t\t\tΕκτύπωση Αποτελεσμάτων")
print("\n* Random Number is : %d \n"%(Random_number))
print("* Time the program ran %d seconds"%time_value)
print("**********************************************************************************")
exit()


