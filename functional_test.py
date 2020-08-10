from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_createAndRetrieveList(self):
        #Check out the homepage
        self.browser.get('http://localhost:8000')
        
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
        inputbox.send_keys('Buy peacock feathres')

        #Pressing enter, the page updates and "!: Buy Peacock Feathers is an item"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr') 
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows), 'New to do item did not appear in table'
        )

        # Enter use peacock feathres to make a fly

        # Page updates

        # Visit the custom URL

        # all works

        #self.browser.quit()
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

