from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_createAndRetrieveList(self):
        #Check out the homepage
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title, 'Wrong title')
        self.fail('Finish the test!')
        #browser = webdriver.Firefox()

        #browser.get('http://localhost:8000')


        #To do is in the title
        #assert 'To-Do' in browser.title


        #SHe can enter an item

        #ENter Buy Peacock feathers

        #Pressing enter, the page updates and "!: Buy Peacock Feathers is an item"

        #Enter use peacock feathres to make a fly

        #Page updates

        #Visit the custom URL

        #all works

        #self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

