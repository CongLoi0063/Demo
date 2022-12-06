# In ra giá trị dấu của một số
import math
sign=lambda x: math.copysign(1,x)
print(sign(-8))
print(sign(8))