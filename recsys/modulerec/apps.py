from django.apps import AppConfig



class RecConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modulerec'



def Data(**kwargs):
    from modulerec.models import Category, Product

    categories = (
        'meat',
        'fish',
        'eggs',
        'milk',
        'vegetables',
        'fruits',
        'fats',
        'cereals',
        'baking',
        'drinks',
    )

    for category_name in categories:
        category, created  = Category.objects.get_or_create(name=category_name)
        if category.name == 'meat':
            Product.objects.get_or_create(name='Корейка свиная запеченная',category=category, protein = 27.23, fats = 13.62, carbohydrates = 0, caloricity = 239.0)
            Product.objects.get_or_create(name='Филе свиное приготовленное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Говядина приготовленная',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Телятина приготовленная',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Куриная грудка запеченная',category=category, protein = 0, fats = 0, carbohydrates = 0)
            Product.objects.get_or_create(name='Куриные ножки запеченные',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Курица жареная',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Голень индейки запеченная',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Грудка индейки вареная',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
        elif category.name == 'fish':
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)
            Product.objects.get_or_create(name='Бедро индейки запеченное',category=category, protein = 0.0, fats = 0.0, carbohydrates = 0)