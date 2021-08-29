import sys

from bitstring import BitArray
from math import log2

def booth(m, r, x, y):
	# Initialize
	totalLength = x + y + 1
	mA = BitArray(int = m, length = totalLength)
	rA = BitArray(int = r, length = totalLength)
	A = mA << (y+1)
	S = BitArray(int = -m, length = totalLength)  << (y+1)
	P = BitArray(int = r, length = y)
	P.prepend(BitArray(int = 0, length = x))
	P = P << 1
	print("Initial values")
	print ("A", A.bin)
	print ("S", S.bin)
	print ("P", P.bin)
	print ("Starting calculation")
	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P = BitArray(int = P.int + A.int, length = totalLength)
			print( "P +  A:", P.bin)
		elif P[-2:] == '0b10':
			P = BitArray(int = P.int +S.int, length = totalLength)
			print ("P +  S:", P.bin)
		P = arith_shift_right(P, 1)
		print ("P >> 1:", P.bin)
	P = arith_shift_right(P, 1)
	print ("P >> 1:", P.bin)
	return P.int

def arith_shift_right(x, amt):
	l = x.len
	x = BitArray(int = (x.int >> amt), length = l)
	return x

# Sample usage: find 86 * 41

Multiplier=int(sys.argv[1])
Mplicand=int(sys.argv[2])
if log2(abs(Multiplier))%1==0:
	s1=int(log2(abs(Multiplier)))
else: s1=int(log2(abs(Multiplier))+1)
if log2(abs(Mplicand))%1==0:
	s2=int(log2(abs(Mplicand)))
else: s2=int(log2(abs(Mplicand))+1)
if s1 > s2: s=s1+1
elif s2 > s1: s = s2+1
else: s=s1+1
#
#s2=int(log2(Mplicand))
#print(Multiplier, Mplicand, s1, s2)

b = booth(Multiplier, Mplicand, s,s)
print( b)

