import unittest
import helpers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TestCrudFlaskr(unittest.TestCase):

    def setUp(self):
        # Get the driver instance
        self.driver = helpers.get_driver()

    ##################################
    # Create the article
    ##################################

    def test_1_create_post(self):

        # Get the driver
        driver = self.driver

        # Login
        helpers.login()

        driver.get(helpers.BASE_URL+'/')
        driver.find_element_by_link_text('New').click()

        title = driver.find_element_by_name('title')
        title.send_keys('Selenium test article 123')

        body = driver.find_element_by_name('body')
        body.send_keys('This is the article text {{!--readmore--}} And this is the rest of the text after readmore')

        # Save the post
        driver.find_element_by_xpath("//input[@value='Save']").click()

        # Verify if the post was successfully saved ..
        postElem = driver.find_element_by_css_selector('.content > article > header > div > h1')
        assert postElem.text == 'Selenium test article 123'


#    ##################################
#    # Update the article
#    ##################################
#
#    def test_2_update_article(self):
#
#        # Get the ID of the saved post
#        self.__class__.postUpdate = driver.find_element_by_css_selector('.content > article > header > a').href
#        driver = self.driver
#
#        # Open the newly created article
#        driver.get(helpers.BASE_URL+'/administrator/article/'+ self.__class__.articleID+'/edit')
#
#        # Press the save button
#        driver.find_element_by_id('save').click()
#
#        # Verify if the article was successfully saved ..
#        messageElem = driver.find_element_by_css_selector('#fouc > div > form:nth-child(1) > div.status-message > div > ul > li')
#        assert messageElem.text == 'Article was successfully saved!'
#
#    ##################################
#    # Trash the article
#    ##################################
#
#    def test_3_trash_article(self):
#
#        driver = self.driver
#
#        # Trash article
#        driver.get(helpers.BASE_URL+'/administrator/article')
#        driver.find_element_by_id('actions_container_' + str(self.__class__.articleID)).click()
#        driver.find_element_by_id('trash_'+str(self.__class__.articleID)).click()
#
#        # Wait for the message to be displayed on the page
#        driver.implicitly_wait(1)  # seconds
#
#        # Verify the article is in the trash
#        message = driver.find_element_by_css_selector('.alert > ul:nth-child(1) > li:nth-child(1)')
#        assert message.text == "The article was successfully trashed!"
