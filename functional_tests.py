from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # notice todo in title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # can type a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # type example "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        # Hit Enter to update
        inputbox.send_keys(Keys.ENTER)

        # Page now lists "1: Buy peacock feathers"
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            'New to-do item did not appear in table'
        )

        # can type another to-do item straight away
        self.fail('Finish the test!')
        # type example "Use peacock feathers to make a fly"

        # site has unique url for list

        # visit that url

        # done


if __name__ == '__main__':
    unittest.main(warnings='ignore')
