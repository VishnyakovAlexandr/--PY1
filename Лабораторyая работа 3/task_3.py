money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0 # количество месяцев, которое можно прожить
p=0
n=money_capital+salary
while n>=0:
    n=n-(spend+spend*increase)
    p+=1
month=p
print (month)