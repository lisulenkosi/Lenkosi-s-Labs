def convert_decimal(number, base):
	alphdig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	decimal = 0
	power = len(number)-1 
	for i in number:
		decimal = decimal + alphdig.index(i) * (base**power)
		power = power - 1
	return decimal
decimals = []
base = int(input())
while True:
	number = input().strip()
	if number == "-1":
		break
	decimals.append(convert_decimal(number,base))
for d in decimals:
	print(d)
	

