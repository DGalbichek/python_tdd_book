from .base import FunctionalTest
from selenium import webdriver


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_for_one_user(self):
        self.browser.get(self.live_server_url)

        # notice to-do in title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # can type a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # type example "Buy peacock feathers"
        # Hit Enter to update
        # Page now lists "1: Buy peacock feathers"
        self.add_list_item('Buy peacock feathers')

        # can type another to-do item straight away
        # type example "Use peacock feathers to make a fly"
        self.add_list_item('Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        self.add_list_item('Buy peacock feathers')

        # she notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site

        ## We use new browser session to make sure that no information of Edith's is coming through
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Francis visits the homepage. No sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list
        self.add_list_item('Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep
