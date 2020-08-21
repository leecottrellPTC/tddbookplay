from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item

# class ItemModelTest(TestCase):
#     def test_saving_and_retrieving_items(self):
#         first_item = Item()
#         first_item.text = 'The first (ever) list item'
#         first_item.save()

#         second_item = Item()
#         second_item.text = 'Item the second'
#         second_item.save()

#         saved_items = Item.objects.all()
#         self.assertEqual(saved_items.count(), 2)

#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item, 'The first (ever) list item')
#         self.assertEqual(second_saved_item, 'Item the second')

# Create your tests here.

#class SmokeTest(TestCase):
#    def test_bad_math(self):
#        self.assertEqual(1 + 1, 3)

class ListViewTest(TestCase):
    def test_displays_all_items(self):
        Item.objects.create(text='itemny 1') #just placeholder stuff
        Item.objects.create(text='itemny 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemny 1')
        self.assertContains(response ,'itemny 2')

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

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
        self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(response.status_code, 302)#302 is redirect
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/') #redirect after the POST

    # def test_displays_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')

    #     response = self.client.get('/')

    #     self.assertIn('itemey 1', response.content.decode())
    #     self.assertIn('itemey 2', response.content.decode())

    class ListViewTest(TestCase):
        def test_uses_list_template(self):
            response = self.client.get('/lists/the-only-list-in-the-world/')
            self.assertTempalteUsed(response, 'list.html')