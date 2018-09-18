import math
[(x0,y0),(x1,y1),(x2,y2)] = [raw_input().split() for _ in xrange(3)]
x0,y0 = float(x0),float(y0)
x1,y1 = float(x1),float(y1)
x2,y2 = float(x2),float(y2)

# first, solve for the center of the circle (p,q)
# to see how I did this, see this math.stackexchange post:
# https://math.stackexchange.com/questions/213658/get-the-equation-of-a-circle-when-given-3-points
a11,a12,a21,a22 = 2*(x0-x1), 2*(y0-y1), 2*(x0-x2), 2*(y0-y2)
b1,b2 = x0**2-x1**2+y0**2-y1**2, x0**2-x2**2+y0**2-y2**2
q = (a21*b1 - a11*b2)/(a21*a12 - a11*a22)
p = (b1 - a12*q)/a11
r2 = (x0 - p)**2 + (y0 - q)**2

# as described here:
# https://math.stackexchange.com/questions/1142644/regular-polygon-determined-by-three-vertices
# we can determine the smallest number of sides given the angles with the center
AB = ((x0 - p)*(x1 - p) + (y0 - q)*(y1 - q))/r2
BC = ((x2 - p)*(x1 - p) + (y2 - q)*(y1 - q))/r2
CA = ((x0 - p)*(x2 - p) + (y0 - q)*(y2 - q))/r2

AOB = 180*math.acos(AB)/math.pi
BOC = 180*math.acos(BC)/math.pi
COA = 180*math.acos(CA)/math.pi

# this is probably too much brute force/slow
n,c1,c2,c3 = 2,0,0,0
while c1 + c2 + c3 != 3 and n <= 100:
	n += 1
	a = 360.0/n
	s1,s2,s3 = AOB/a, BOC/a, COA/a
	c1 = int(math.fabs(round(s1) - s1) < 0.001)
	c2 = int(math.fabs(round(s2) - s2) < 0.001)
	c3 = int(math.fabs(round(s3) - s3) < 0.001)

print n*r2*math.sin(2*math.pi/n)/2
