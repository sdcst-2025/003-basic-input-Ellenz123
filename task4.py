#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

h=input("What is the height:")
h=float(h)
r=input("What is the radius:")
r=float(r)
A=3.14*r**2+r*3.14*((r**2+h**2)**(1/2))
print(f"surface area is {A}")