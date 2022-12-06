def kiemtrasonguyento(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        return True
        return False
x=int(input("nhập số x :"))
print(kiemtrasonguyento(x))