def convert_base(decimal, base):
	if decimal == 0 or base == 0:
		return 0
	alphdig = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ''
	while decimal:
		result = alphdig[decimal%base]+ result
		decimal = decimal//base
	return result
results=[]
base = int(input())
while True:
	number = int(input())
	if number == -1 :
		break
	results.append(convert_base(number, base))
for result in results:
	print(result)
	
