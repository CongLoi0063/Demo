import numbers
x = int(input("Nhập vào một số x: "))
n = int(input("Nhập vào một số n: "))
left = pow(x,2) + x + 1
right = pow(x,2) - x + 1
print("kết quả phép tính A = (x^2 + x + 1)^n + (x^2 - x + 1)^n là:  ",(pow(left,n) + pow(right,n) ))