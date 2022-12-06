# Tính chỉ số BMI
chieucao=float(input("nhập chiều cao (m) :"))
cannang=float(input("Nhập cân nặng (kg) :"))
BMI=cannang/(chieucao**2)
print("Chỉ số BMI của bạn :",BMI)
if BMI < 18.5:
    print("Thiếu chất")
elif BMI < 24.99:
    print("Cân đối")
elif BMI<=25:
    print("Béo rồi")
else:
    print("Sumô!!!")