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

def applyfunction(b, seq):
	return sum([int(item)*b[elem] for elem,item in enumerate(seq)])

def applyknapsack(num, seq):
	res = ''

	for elem in seq[::-1]:
		if num >= elem:
			res += '1'
			num = num - elem
		else:
			res += '0'

	if num > 0:				# no solution
		return ''

	res = res[::-1]

	return res

def subdivide(seq, n):
	blocks = []
	i = 0
	while 1:
		if i*n >= len(seq):
			break
		blocks.append(seq[(i*n):(i*n+n)])
		i += 1

	return blocks

def showpublickey(a, m, w):
	b = [w*elem%m for elem in a]

	return tuple(b)

def encrypt(b, m, message):
	n = len(b)
	seq = ''
	for item in message:
		equiv = letters.find(item)		# get decimal equivalent
		equiv = bin(equiv)[2:]			# get binary equivalent
		equiv = equiv.zfill(5)			# prepend with zeros
		seq += equiv

	while (len(seq) % n != 0):
		seq += '10111'				# append 'X'

	blocks = subdivide(seq, n)

	blocks = [applyfunction(b,elem)%m for elem in blocks]

	return tuple(blocks)

def decrypt(b, m, w, message):
	r, s, w_inv = extended_gcd(m, w)		# get inverse of w
	v = [elem*w_inv%m for elem in message]		# decrypt message

	a = [w_inv*elem%m for elem in b]		# solve for the superincreasing sequence
	if not issuperincreasing(a):
		print('Solved sequence is not superincreasing. Please run code again.')
		return ''
	if not ismodulusvalid(m, a):
		print('Modulus is not greater than solved 2*a_n. Please run code again.')
		return

	v = [applyknapsack(elem, a) for elem in v]

	if '' in v:
		print('Knapsack problem was not solved. Please run code again.')
		return ''

	res = ''.join(v)

	blocks = subdivide(res, 5)

	blocks = [int(elem,2) for elem in blocks]	# convert to decimal

	blocks = [letters[elem] for elem in blocks]
	blocks = ''.join(blocks)

	return blocks

def main():
	resp = input('[S]how public key, [E]ncrypt, or [D]ecrypt? ').upper()
	if resp not in ('S', 'E', 'D'):
		print('Mode not recognized. Please run code again.')
		return

	if resp in ('S'):
		seq = tuple(int(n.strip().strip('(').strip(')').strip()) for n in input('Type superincreasing sequence: ').split(','))
	else:
		seq = tuple(int(n.strip().strip('(').strip(')').strip()) for n in input('Type public key: ').split(','))
	if resp in ('S'):
		if not issuperincreasing(seq):
			print('Sequence is not superincreasing. Please run code again.')
			return

	m = int(input('Type modulus: '))
	if resp in ('S'):
		if not ismodulusvalid(m, seq):
			print('Modulus is not greater than 2*a_n. Please run code again.')
			return

	if resp in ('S', 'D'):
		w = int(input('Type private key: '))
	if resp in ('S', 'D'):
		if gcd(m, w) > 1:
			print('Private key is NOT relatively prime with modulus. Please run code again.')
			return

	if resp in ('E'):
		message = input('Type message: ').upper()
	elif resp in ('D'):
		message = tuple(int(n.strip().strip('(').strip(')').strip()) for n in input('Type message: ').split(','))

	if resp in ('S'):
		print(showpublickey(seq, m, w))
	if resp in ('E'):
		print(encrypt(seq, m, message))
	elif resp in ('D'):
		print(decrypt(seq, m, w, message))

if __name__ == '__main__':
	try:
		main()
	except ValueError:
		print('Did not respond to expected data type. Please run code again.')
