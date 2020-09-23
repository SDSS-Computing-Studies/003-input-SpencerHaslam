#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 84.8230016469
import math
radius = input("Enter radius")
x = int(radius)
cube = pow(x, 3)
volume = 4 / 3 * math.pi * cube
y = str(volume)
print("the volume is " + y)
