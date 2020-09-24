#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.
import math
vol = input("Emnter volume")
x = float(vol)
z = 4 * math.pi
a = x / z
c = 3 * a
e = 1.0 / 3
b = c ** e
y = str(b)
print("the radius is " + y)
