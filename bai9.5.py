import math
s=lambda x ,n:math.pow(math.pow(x,2)+x+1 ,n)+math.pow(math.pow(x,2)-x+1 ,n)
print("S =",s(3,4))