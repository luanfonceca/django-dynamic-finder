from django.test import TestCase

from .models import Product

class ProductTest(TestCase):
    fixtures = ["products.json"]

    def test_should_can_be_getted_by_name(self):
        expected = Product.objects.get(name="Diamond")
        
        self.assertEqual(
            Product.objects.get_by_name("Diamond"),
            expected
        )

    def test_should_can_be_filtered_by_name(self):
        self.assertQuerysetEqual(
            Product.objects.filter_by_name("Diamond"),
            ["<Product: #1 - Diamond>"]
        )

    def test_should_can_be_excluded_by_name(self):
        self.assertQuerysetEqual(
            Product.objects.exclude_by_name("Diamond"),
            ["<Product: #2 - Gold>", "<Product: #3 - Silver>"]
        )