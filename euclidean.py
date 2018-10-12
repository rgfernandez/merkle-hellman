def gcd(a, b):
	c = max(a, b)
	d = min(a, b)

	if d == 0:
		return c

	return gcd(d, c%d)

if __name__ == '__main__':
	a = input('Enter first number: ')
	b = input('Enter second number: ')

	c = gcd(int(a), int(b))
	print(f'The GCD of {a} and {b} is {c}')
