# Python program to calculate all dividers of a given number
from __future__ import print_function
import time

number = 2 # initial dummy value to keep the while-loop running
while (number > 1):
	number = int(input("number to find all dividers: "))
	if (number <= 1):
		quit()

	count = 0
	start = time.time()
	last_time = start
	for i in range(2,number//2):
	    if (number % i) == 0:
	        print(i)
	        count=count+1

	    if (time.time() - last_time > 30.0):
	    	print(".")
	    	last_time = time.time()

	if (count == 0):
		print("No dividers found.")
		print("Congratulations!", number, "is prime!")
	else:
		print("Found", count, "dividers")
	end = time.time()

	print ("finding them took ", end - start, " seconds")