x=int(input("nhập số nguyên x :"))
tong = 0
for i in range(1,x-1):
    if (x%i==0):
        tong+=i
if (tong==x):
         print(x,"là số hoàn hảo")
else:
        print(x,"là số không hoàn hảo")