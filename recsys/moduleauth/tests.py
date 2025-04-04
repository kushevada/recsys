from django.test import TestCase
from modulerec.models import Product, Category
from modulerec.apps import FilterProducts


# Create your tests here.
class ProductPurposeTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="meat")
        Product.objects.create(name="Low Calorie Meat", category=category,
                               proteins=30, fats=3, carbohydrates=0, caloricity=140)
        Product.objects.create(name="High Protein Meat", category=category,
                               proteins=35, fats=10, carbohydrates=0, caloricity=250)
        Product.objects.create(name="Balanced Meat", category=category,
                               proteins=25, fats=8, carbohydrates=0, caloricity=180)

    def test_assign_product_purposes(self):
        FilterProducts()

        low_calorie_meat = Product.objects.get(name="Low Calorie Meat")
        high_protein_meat = Product.objects.get(name="High Protein Meat")
        balanced_meat = Product.objects.get(name="Balanced Meat")

        self.assertTrue(low_calorie_meat.is_for_weight_loss)
        self.assertFalse(low_calorie_meat.is_for_weight_gain)
        self.assertFalse(low_calorie_meat.is_fow_weight_main)

        self.assertFalse(high_protein_meat.is_for_weight_loss)
        self.assertTrue(high_protein_meat.is_for_weight_gain)
        self.assertFalse(high_protein_meat.is_fow_weight_main)

        self.assertFalse(balanced_meat.is_for_weight_loss)
        self.assertFalse(balanced_meat.is_for_weight_gain)
        self.assertTrue(balanced_meat.is_fow_weight_main)