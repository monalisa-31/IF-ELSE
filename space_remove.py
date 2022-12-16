num=int(input('enter your num'))
c=0
i=1
while i<=num:
	if num%i==0:
		c=c+1
		i=i+1
	if(c==2):
		print(num,'prime number')
	else:
		print(num,'not prime number')
