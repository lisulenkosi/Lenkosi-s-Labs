import math
import sys

mode = input()
base = int(input())
alphdig= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if mode == "encrypt":
	mess = sys.stdin.read()
	lists=[]
	for char in mess:
		mess1= ord(char)
		lists.append(mess1)
	for num in lists:
		x = num
		power = int(math.log(x)//math.log(base))
		base_power = base**power
		
		for v in range(power,-1,-1):
			y = x 
			base_power = base**v
			quotient = y//base_power
			remainder = y % base_power
			x = remainder 
			print(alphdig[quotient],end="")
		print(" ",end="")	
	print()
if mode == "decrypt":
	w = input().split()
	for i in w:
		length = len(i)
		exponent =length -1
		tot = 0
		for word in i:
			position = alphdig.index(word)
			base_exponent = base**exponent
			num = position*base_exponent
			tot += num
			exponent -=1
		w = chr(tot)
		print(w,end="")
	print()
		
	
		
