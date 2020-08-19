from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        #request = HttpRequest()
        #response = home_page(request)
        response = self.client.get('/')
        #html = response.content.decode('utf8')
        #self.assertTrue(html.startswith('<html>'))
        #self.assertIn('<title>To-Do Lists</title>',html)
        #self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
