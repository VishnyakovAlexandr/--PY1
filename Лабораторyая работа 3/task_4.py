salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
n = 0
p = spend
need_money = 0  # количество денег, чтобы прожить 10 месяцев
while n != months:
    n += 1
    need_money = need_money + p - salary
    p = p * 1.03  # проценты за 9 месяцев, тк первый месяц без них


print(round(need_money))