from euclidean import gcd
from extended_euclidean import extended_gcd

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def issuperincreasing(sequence):
	ssum = 0
	
	for elem in sequence:
		if elem <= ssum:
			return False
		ssum += elem

	return True

def ismodulusvalid(modulus, sequence):
	return modulus > (2*sequence[-1])

def main():
	resp = input('[E]ncrypt or [D]ecrypt? ').upper()
	if resp not in ('E', 'D'):
		print('Mode not recognized. Please run code again.')
		return

	a = tuple(int(n.strip().strip('(').strip(')').strip()) for n in input('Type sequence a: ').split(','))
	if not issuperincreasing(a):
		print('Sequence is not superincreasing. Please run code again.')
		return

	m = int(input('Type modulus m: '))
	if not ismodulusvalid(m, a):
		print('Modulus is not greater than 2*a_n. Please run code again.')
		return

	w = int(input('Type private key w: '))
	print(gcd(m,w))
	if gcd(m, w) > 1:
		print('Private key is NOT relatively prime with modulus. Please run code again.')
		return

	print('Passed all checks')

if __name__ == '__main__':
	try:
		main()
	except ValueError:
		print('Did not respond to expected data type. Please run code again.')
