def extended_gcd(a, b):
	c = max(a, b)
	d = min(a, b)

	s = 0; old_s = 1
	t = 1; old_t = 0

	while True:
		q = int(c / d)
		r = c % d

		print(f'{r} = {c} - {q}({d})')

		(old_s, s) = (s, old_s - q*s)
		(old_t, t) = (t, old_t - q*t)

		print(f'  {r} = {s}({a}) + {t}({b})')

		if (r == 0):
			return (d, old_s, old_t)

		c = d
		d = r

if __name__ == '__main__':
	a = int(input('Enter first number: '))
	b = int(input('Enter second number: '))

	if (a < b):
		(a, b) = (b, a)

	(c, d, e) = extended_gcd(a, b)
	print(f'The GCD of {a} and {b} is {c}. The solution to {a}*x+{b}*y={c} is ({d},{e})')
