salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
podushka = spend - salary
for i in range(1,months):
    spend += spend * increase
    podushka += spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(podushka))
