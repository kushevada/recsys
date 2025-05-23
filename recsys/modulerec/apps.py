from django.apps import AppConfig



class RecConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modulerec'

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(self.load_initial_data)

    def load_initial_data(self, sender, **kwargs):
        from .products import Data
        Data()
        self.filter_products()

    def filter_products(self):
        from modulerec.models import Product

        products = Product.objects.all()

        for product in products:
            if product.caloricity <= 150.0 and product.fats <= 5.0:
                product.is_for_weight_main = False
                product.is_for_weight_gain = False
                product.is_for_weight_loss = True
            elif product.caloricity > 200.0 and product.proteins >= 25.0:
                product.is_for_weight_main = False
                product.is_for_weight_gain = True
                product.is_for_weight_loss = False
            else:
                product.is_for_weight_main = True
                product.is_for_weight_gain = False
                product.is_for_weight_loss = False
            product.save()