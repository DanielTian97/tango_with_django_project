from django.test import TestCase
from rango.models import Category
from django.urls import reverse

# Create your tests here.
class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        Ensures the number of views received for a Category are positive or zero
        """
        category = Category(name='test', views=-1, likes=0)
        category.save()
        
        self.assertEqual((category.views >= 0), True)
        
    def test_slug_line_creation(self):
        """
        Checks to make sure that when a category is created, an appropriate slug is created.
        Example: "Random Category String" should be "random-category-string".
        """
        category = Category(name='Random Category String')
        category.save()
        
        self.assertEqual(category.slug, 'random-category-string')
        
class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no categories exist, the appropriate message should be displayed.
        """
        response = self.client.get(reverse('rango:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])