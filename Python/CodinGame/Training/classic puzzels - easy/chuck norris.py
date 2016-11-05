import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = raw_input()

# Write an action using print
print >> sys.stderr, message

bin_message = [bin(ord(ch))[2:] for ch in list(message)]
print >> sys.stderr, bin_message

c_n_arry = []

# 0 at the start of binary are ignored normaly
bin_with_0 = ["0"*(7-len(bin))+bin for bin in bin_message]
print >> sys.stderr, bin_with_0
binary = "".join(bin_with_0)

c_n_code = ""
last_bit = None
last_bit_length = 0
for bit in list(binary):
	if bit == last_bit:
		last_bit_length += 1
	else:
		if last_bit_length != 0:
			c_n_code += "00 " if last_bit == "0" else "0 "
			c_n_code += last_bit_length*"0"
			c_n_code += " "
		last_bit_length = 1
		last_bit = bit
else:
	if last_bit_length != 0:
		c_n_code += "00 " if last_bit == "0" else "0 "
		c_n_code += last_bit_length*"0"
		# c_n_code += " "
	last_bit_length = 1
	last_bit = bit
c_n_arry.append(c_n_code)

print >> sys.stderr, c_n_arry

#print "  ".join(c_n_arry)
print "".join(c_n_arry)
