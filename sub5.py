def convert_base(decimal, base):
	alphdig ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result=""
	while decimal:
		result = alphdig[decimal % base] + result
		decimal = decimal // base 
	return result 
	
def convert_decimal(number, base):
	alphdig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	decimal = 0
	power = len(number)-1 
	for i in number:
		decimal = decimal + alphdig.index(i) * (base**power)
		power = power - 1
	return decimal
mode = input().strip()
base = int(input())
message = input().strip()

if mode =="encrypt":
	encrypted_mess = [ convert_base(ord(chr), base) for chr in message]
	print(' '.join(encrypted_mess))
elif mode =="decrypt":
	numbers = message.split()
	decrypted_mess =[chr(convert_decimal(num, base)) for num in numbers]
	print(' '.join(decrypted_mess))
	
