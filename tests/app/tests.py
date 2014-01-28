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
            [
                "<Product: #2 - Gold>", 
                "<Product: #3 - Silver>", 
                "<Product: #4 - Bronze>"
            ]
        )

    def test_should_can_be_possible_to_use_or_statements_in_filter(self):
        self.assertQuerysetEqual(
            Product.objects.filter_by_name_or_name("Diamond", "Gold"),
            [
                "<Product: #1 - Diamond>", 
                "<Product: #2 - Gold>"
            ]
        )

    def test_should_can_be_possible_to_use_or_statements_in_exclude(self):
        self.assertQuerysetEqual(
            Product.objects.exclude_by_name_or_id("XXX", 1),
            [
                "<Product: #2 - Gold>", 
                "<Product: #3 - Silver>", 
                "<Product: #4 - Bronze>"
            ]
        )

    def test_should_can_be_possible_to_use_multiple_or_statements(self):
        self.assertQuerysetEqual(
            Product.objects.filter_by_name_or_id_or_name("Diamond", 2, "Silver"),
            [
                "<Product: #1 - Diamond>", 
                "<Product: #2 - Gold>", 
                "<Product: #3 - Silver>"
            ]
        )
