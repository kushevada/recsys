def Data():
    from modulerec.models import Category, Product

    if Category.objects.exists():
        return
    if Product.objects.exists():
        return

    categories = {
        'meat': 'Мясо и птица',
        'fish': 'Рыба',
        'eggs': 'Яичная продукция',
        'milk': 'Молочная продукция',
        'vegetables': 'Овощи',
        'fruits': 'Фрукты и ягоды',
        'fats': 'Жиры и масла',
        'cereals': 'Крупы и злаки',
        'baking': 'Выпечка',
    }

    for category_name, ru_name in categories.items:
        category, created = Category.objects.get_or_create(name=category_name, defaults={'ru_name': ru_name})
        if not created and category.ru_name != ru_name:
            category.ru_name = ru_name
            category.save()

        if category.name == 'meat':
            Product.objects.get_or_create(name='Корейка свиная запеченная' ,
                category=category, proteins = 27.23, fats = 13.62, carbohydrates = 0, caloricity = 239.0)
            Product.objects.get_or_create(name='Филе свиное приготовленное' ,
                category=category, proteins = 29.47, fats = 9.44, carbohydrates = 0, caloricity = 211.0)
            Product.objects.get_or_create(name='Говядина приготовленная' ,
                category=category, proteins = 29.9, fats = 8.37, carbohydrates = 0, caloricity = 203.0)
            Product.objects.get_or_create(name='Телятина приготовленная' ,
                category=category, proteins = 31.9, fats = 6.58, carbohydrates = 0, caloricity = 196.0)
            Product.objects.get_or_create(name='Куриная грудка запеченная' ,
                category=category, proteins = 30.54, fats = 3.17, carbohydrates = 0, caloricity = 151.0)
            Product.objects.get_or_create(name='Куриные ножки запеченные' ,
                category=category, proteins = 24.03, fats = 8.99, carbohydrates = 0, caloricity = 184.0)
            Product.objects.get_or_create(name='Курица жареная' ,
                category=category, proteins = 30.57, fats = 9.12, carbohydrates = 0, caloricity = 219.0)
            Product.objects.get_or_create(name='Бедро индейки запеченное' ,
                category=category, proteins = 27.71, fats = 6.04, carbohydrates = 0, caloricity = 165.0)
            Product.objects.get_or_create(name='Голень индейки запеченная' ,
                category=category, proteins = 30.13, fats = 2.08, carbohydrates = 0, caloricity = 139.0)
            Product.objects.get_or_create(name='Грудка индейки вареная' ,
                category=category, proteins = 30.13, fats = 2.08, carbohydrates = 0, caloricity = 147.0)
        elif category.name == 'fish':
            Product.objects.get_or_create(name='Анчоусы консервированные' ,
                category=category, proteins = 28.89, fats = 9.71, carbohydrates = 0, caloricity = 210.0)
            Product.objects.get_or_create(name='Горбуша запеченная' ,
                category=category, proteins = 24.58, fats = 5.28, carbohydrates = 0, caloricity = 153.0)
            Product.objects.get_or_create(name='Окунь запеченный' ,
                category=category, proteins = 24.18, fats = 4.73, carbohydrates = 0, caloricity = 146.0)
            Product.objects.get_or_create(name='Осетр запеченный' ,
                category=category, proteins = 20.7, fats = 5.18, carbohydrates = 0, caloricity = 135.0)
            Product.objects.get_or_create(name='Палтус запеченный' ,
                category=category, proteins = 22.54, fats = 1.61, carbohydrates = 0, caloricity = 111.0)
            Product.objects.get_or_create(name='Сельд запеченная' ,
                category=category, proteins = 23.03, fats = 11.59, carbohydrates = 0, caloricity = 203.0)
            Product.objects.get_or_create(name='Семга запеченная' ,
                category=category, proteins = 25.44, fats = 8.13, carbohydrates = 0, caloricity = 182.0)
            Product.objects.get_or_create(name='Скумбрия запеченная' ,
                category=category, proteins = 23.85, fats = 17.81, carbohydrates = 0, caloricity = 262.0)
            Product.objects.get_or_create(name='Треска запеченная' ,
                category=category, proteins = 20.42, fats = 0.25, carbohydrates = 0, caloricity = 84.0)
            Product.objects.get_or_create(name='Тунец' ,
                category=category, proteins = 19.44, fats = 0.96, carbohydrates = 0, caloricity = 86.0)
        elif category.name == 'eggs':
            Product.objects.get_or_create(name='Яйцо куриное вареное' ,
                category=category, proteins = 12.58, fats = 10.61, carbohydrates = 1.12, caloricity = 155.0)
            Product.objects.get_or_create(name='Яичный белок' ,
                category=category, proteins = 10.09, fats = 0.17, carbohydrates = 0.73, caloricity = 52.0)
            Product.objects.get_or_create(name='Яичный желток' ,
                category=category, proteins = 15.86, fats = 26.54, carbohydrates = 3.59, caloricity = 322.0)
            Product.objects.get_or_create(name='Яйцо гусиное' ,
                category=category, proteins = 13.87, fats = 13.27, carbohydrates = 1.35, caloricity = 185.0)
            Product.objects.get_or_create(name='Яйцо перепелиное' ,
                category=category, proteins = 13.05, fats = 11.09, carbohydrates = 0.41, caloricity = 158.0)
        elif category.name == 'milk':
            Product.objects.get_or_create(name='Молоко' ,
                category=category, proteins = 3.28, fats = 3.66, carbohydrates = 4.65, caloricity = 64.0)
            Product.objects.get_or_create(name='Кефир' ,
                category=category, proteins = 3.79, fats = 0.93, carbohydrates = 4.48, caloricity = 41.0)
            Product.objects.get_or_create(name='Сыр сливочный' ,
                category=category, proteins = 6.15, fats = 34.44, carbohydrates = 5.52, caloricity = 350.0)
            Product.objects.get_or_create(name='Сметана' ,
                category=category, proteins = 3.5, fats = 10.6, carbohydrates = 7.1, caloricity = 136.0)
            Product.objects.get_or_create(name='Творог' ,
                category=category, proteins = 13.05, fats = 2.27, carbohydrates = 4.76, caloricity = 81.0)
            Product.objects.get_or_create(name='Сыр гауда' ,
                category=category, proteins = 24.94, fats = 27.44, carbohydrates = 2.22, caloricity = 356.0)
            Product.objects.get_or_create(name='Сыр моцарелла' ,
                category=category, proteins = 23.75, fats = 19.78, carbohydrates = 5.58, caloricity = 295.0)
            Product.objects.get_or_create(name='Сыр чеддер' ,
                category=category, proteins = 22.87, fats = 33.31, carbohydrates = 3.09, caloricity = 404.0)
            Product.objects.get_or_create(name='Масло сливочное' ,
                category=category, proteins = 0.28, fats = 99.48, carbohydrates = 0.0, caloricity = 876.0)
            Product.objects.get_or_create(name='Молоко сгущенное' ,
                category=category, proteins = 7.91, fats = 8.7, carbohydrates = 54.4, caloricity = 321.0)
        elif category.name == 'vegetables':
            Product.objects.get_or_create(name='Картофель запеченный' ,
                category=category, proteins = 1.96, fats = 0.1, carbohydrates = 21.55, caloricity = 93.0)
            Product.objects.get_or_create(name='Картофель варёный' ,
                category=category, proteins = 1.71, fats = 0.1, carbohydrates = 20.01, caloricity = 86.0)
            Product.objects.get_or_create(name='Морковь' ,
                category=category, proteins = 0.93, fats = 0.24, carbohydrates = 6.78, caloricity = 41.0)
            Product.objects.get_or_create(name='Огурцы' ,
                category=category, proteins = 0.65, fats = 0.11, carbohydrates = 3.63, caloricity = 15.0)
            Product.objects.get_or_create(name='Помидоры' ,
                category=category, proteins = 0.88, fats = 0.2, carbohydrates = 3.89, caloricity = 18.0)
            Product.objects.get_or_create(name='Брокколи' ,
                category=category, proteins = 2.6, fats = 0.3, carbohydrates = 3.9, caloricity = 31.0)
            Product.objects.get_or_create(name='Перец болгарский' ,
                category=category, proteins = 1.8, fats = 0.0, carbohydrates = 6.0, caloricity = 38.0)
            Product.objects.get_or_create(name='Цветная капуста' ,
                category=category, proteins = 2.5, fats = 0.3, carbohydrates = 4.2, caloricity = 30.0)
            Product.objects.get_or_create(name='Кабачок' ,
                category=category, proteins = 0.6, fats = 0.3, carbohydrates = 4.6, caloricity = 24.0)
            Product.objects.get_or_create(name='Баклажан' ,
                category=category, proteins = 1.2, fats = 0.1, carbohydrates = 4.5, caloricity = 4.5)
            Product.objects.get_or_create(name='Томаты' ,
                category=category, proteins = 0.9, fats = 0.2, carbohydrates = 2.7, caloricity = 18.0)
            Product.objects.get_or_create(name='Горошек зеленый' ,
                category=category, proteins = 5.4, fats = 0.2, carbohydrates = 13.6, caloricity = 75.0)
            Product.objects.get_or_create(name='Свекла' ,
                category=category, proteins = 2.0, fats = 0.0, carbohydrates = 9.0, caloricity = 40.0)
            Product.objects.get_or_create(name='Салат листовой' ,
                category=category, proteins = 1.5, fats = 0.2, carbohydrates = 2.3, caloricity = 17.0)
            Product.objects.get_or_create(name='Щавель' ,
                category=category, proteins = 2.0, fats = 0.7, carbohydrates = 3.2, caloricity = 22.0)
        elif category.name == 'fruits':
            Product.objects.get_or_create(name='Апельсины' ,
                category=category, proteins = 0.94, fats = 0.12, carbohydrates = 11.75, caloricity = 47.0)
            Product.objects.get_or_create(name='Бананы' ,
                category=category, proteins = 1.09, fats = 0.33, carbohydrates = 22.84, caloricity = 89.0)
            Product.objects.get_or_create(name='Киви' ,
                category=category, proteins = 1.14, fats = 0.52, carbohydrates = 14.66, caloricity = 61.0)
            Product.objects.get_or_create(name='Яблоки' ,
                category=category, proteins = 0.26, fats = 0.17, carbohydrates = 13.81, caloricity = 52.0)
            Product.objects.get_or_create(name='Авокадо' ,
                category=category, proteins = 2.0, fats = 14.66, carbohydrates = 8.53, caloricity = 160.0)
            Product.objects.get_or_create(name='Слива' ,
                category=category, proteins = 0.7, fats = 0.28, carbohydrates = 11.42, caloricity = 46.0)
            Product.objects.get_or_create(name='Голубика' ,
                category=category, proteins = 0.74, fats = 0.33, carbohydrates = 14.49, caloricity = 57.0)
            Product.objects.get_or_create(name='Виноград' ,
                category=category, proteins = 0.72, fats = 0.16, carbohydrates = 18.1, caloricity = 69.0)
            Product.objects.get_or_create(name='Грейпфрут' ,
                category=category, proteins = 0.8, fats = 0.0, carbohydrates = 7.5, caloricity = 37.0)
            Product.objects.get_or_create(name='Ананас' ,
                category=category, proteins = 0.3, fats = 0.1, carbohydrates = 11.8, caloricity = 52.0)
        elif category.name == 'fats':
            Product.objects.get_or_create(name='Масло авокадо' ,
                category=category, proteins = 0.0, fats = 100.0, carbohydrates = 0.0, caloricity = 884.0)
            Product.objects.get_or_create(name='Масло кокосовое' ,
                category=category, proteins = 0.0, fats = 99.06, carbohydrates = 0.0, caloricity = 892.0)
            Product.objects.get_or_create(name='Масло льняное' ,
                category=category, proteins = 0.11, fats = 99.98, carbohydrates = 0.0, caloricity = 884.0)
            Product.objects.get_or_create(name='Масло оливковое' ,
                category=category, proteins = 0.0, fats = 100.0, carbohydrates = 0.0, caloricity = 884.0)
            Product.objects.get_or_create(name='Масло подсолнечное' ,
                category=category, proteins = 0.0, fats = 100.0, carbohydrates = 0.0, caloricity = 884.0)
        elif category.name == 'cereals':
            Product.objects.get_or_create(name='Булгур' ,
                category=category, proteins = 12.3, fats = 1.3, carbohydrates = 63.4, caloricity = 342.0)
            Product.objects.get_or_create(name='Гречневая крупа' ,
                category=category, proteins = 12.6, fats = 3.3, carbohydrates = 57.1, caloricity = 308.0)
            Product.objects.get_or_create(name='Рис' ,
                category=category, proteins = 6.9, fats = 1.0, carbohydrates = 72.2, caloricity = 325.0)
            Product.objects.get_or_create(name='Овсяная крупа' ,
                category=category, proteins = 12.3, fats = 6.1, carbohydrates = 59.5, caloricity = 342.0)
            Product.objects.get_or_create(name='Макароны' ,
                category=category, proteins = 10.4, fats = 1.1, carbohydrates = 69.7, caloricity = 337.0)
        elif category.name == 'baking':
            Product.objects.get_or_create(name='Хлеб ржаной' ,
                category=category, proteins = 8.5, fats = 3.3, carbohydrates = 48.3, caloricity = 259.0)
            Product.objects.get_or_create(name='Хлебцы ржаные' ,
                category=category, proteins = 7.9, fats = 1.3, carbohydrates = 82.2, caloricity = 366.0)
            Product.objects.get_or_create(name='Хлеб белый пшеничный' ,
                category=category, proteins = 10.67, fats = 4.53, carbohydrates = 47.54, caloricity = 274.0)
            Product.objects.get_or_create(name='Блины' ,
                category=category, proteins = 5.2, fats = 2.5, carbohydrates = 36.7, caloricity = 194.0)
