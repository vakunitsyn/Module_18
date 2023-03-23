ticket = int(input('Введите количество билетов: '))
visitor_age = []

for i in range(0, ticket):
    visitor = int(input(f'Введите возраст участника {i + 1}: '))
    visitor_age.append(visitor)

    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    full_priсe = sum(map(price, visitor_age))

discount_priсe = int(full_priсe * 0.9)

if ticket <= 3:
    print('Полная стоимость билетов: ', full_priсe, "рублей")
else:
    print('Стоимость билетов включая скидку 10% за количество, больше трех участников: ', discount_priсe, "рублей")