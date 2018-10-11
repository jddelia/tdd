from selenium import webdriver
import unittest

class NewVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_later(self):
        # John heard about a new "to-do" list app,
        # he goes to the website.
        self.browser.get("http://localhost:8000")
        #self.browser.get("http://localhost:8000")

        # He notices that the word "To-Do" is in the title.
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # The app invites John to make an entry.

        # He types "Study for exam".

        # When hit hits enter, the page updates with the entry
        # on the page as an item.

        # The box for making an entry is still there, and John
        # makes another entry: "Buy new shoes".

        # He presses enter once more, and the page updates with
        # that entry as an item in the list.

        # John checks to see if the site will save his info, and
        # notices that the site has generated a unique URL for him.

        # He checks that URL, and it works.

        # John is satisfied.

if __name__ == "__main__":
    unittest.main()
