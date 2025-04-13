n=int(input("Начальное число: "))
system=int(input("В какую систему переводим: "))
s=""
nums=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"] #Это код из десятичной в любую
while n!=0:
    ost =n % system
    s=str(nums[ost])+s
    n//= system
print(s)