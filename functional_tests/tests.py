from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    #HELPER FUNCTIONS
    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_for_one_user(self):
        #Check out the homepage
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)
        
        #self.fail('Finish the test!')
        #browser = webdriver.Firefox()

        #browser.get('http://localhost:8000')


        #To do is in the title
        #assert 'To-Do' in browser.title
        self.assertIn('To-Do', self.browser.title, 'Wrong title')
        header_text = self.browser.find_element_by_tag_name('h1').text 
        self.assertIn('To-Do', header_text)

        #SHe can enter an item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )


        #ENter Buy Peacock feathers
        inputbox.send_keys('Buy peacock feathers')
        #time.sleep(10)
        #Pressing enter, the page updates and "!: Buy Peacock Feathers is an item"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)#longer numbers to avoid the stale errors

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        #time.sleep(10)
        #Pressing enter, the page updates and "!: Buy Peacock Feathers is an item"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr') 
        #self.assertTrue(
        #    any(row.text == '1: Buy peacock feathers' for row in rows), 
        #    f"New to do item did not appear in table. Contents were:\n{table.text}"
        #)
        # self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        # self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Enter use peacock feathres to make a fly

        # Page updates

        # Visit the custom URL

        # all works

        #self.browser.quit()
        #self.fail('Finish the test!')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        #starts a new to do lost
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #she notices that the list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.
        
        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc

        #now francis visits the site. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    # Satisfied, they both go back to sleep


#def test_can_start_a_list_and_retrieve_it_later(self):
    #self.browser.get(self.live_server_url)

#SHE VISITS that URL - her to do list is still there

#stisfied, she goes to sleep