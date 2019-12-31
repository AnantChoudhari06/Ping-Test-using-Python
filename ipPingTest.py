#!/usr/bin/env python
import os

list=[]
n=int(input("Enter the number of IPs to test"))
for i in range(0,n):
	print("Entern the IP address", i+1)
	val=raw_input()
	list.append(val)

print("================================")
print("IP List is :")
for i in list:
	print(i)

for i in list:
	print("================================")
	response = os.system("ping"+" "  + "-c" + " " + "1"  + " " +i)
	if response == 0:
  		print i, 'is up!'
	else:
  		print i, 'is Down!'
