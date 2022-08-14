from selenium import webdriver
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
        self.fail('Finish the test!')

        # can type a todo item straight away

        # type example "Buy peacock feathers"

        # Hit Enter to update

        # Page now lists "1: Buy peacock feathers"

        # can type another todo item straight away

        # type example "Use peacock feathers to make a fly"

        # site has unique url for list

        # visit that url

        # done


if __name__ == '__main__':
    unittest.main(warnings='ignore')
