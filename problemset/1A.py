import math

(n,m,a) = [float(i) for i in raw_input().split()]

print int(math.ceil(m/a)*math.ceil(n/a))
