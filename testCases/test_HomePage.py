import time

from PageObjects.HomePage import HomePage
from PageObjects.RegistrationPage import Login


class Test001:
    base_url = "http://automationpractice.pl"

    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        # # self.hp.check_title()
        # # self.hp.click_sign_in()
        #
        # time.sleep(2)
        # self.hp.click_tops()
        #
        # self.hp.click_cart()
        # # self.hp.click_blog_button()
        # self.hp.click_summerdresses_2()
        # self.hp.click_contact()
        # self.hp.click_blouses()
        # self.hp.click_home()
        # time.sleep(2)
        # # self.hp.clickslider()
        # self.hp.click_imglnk_1()
        # self.hp.previous_page()
        # self.hp.click_imglnk_2()
        # self.hp.previous_page()
        # self.hp.click_imglnk_3()
        # self.hp.previous_page()
        # self.hp.click_imglnk_4()
        # self.hp.previous_page()
        # self.hp.click_imglnk_5()
        # self.hp.previous_page()
        # self.hp.click_imglnk_6()
        # self.hp.previous_page()
        # self.hp.click_imglnk_7()
        # self.hp.previous_page()
        # self.hp.click_fb()
        # time.sleep(2)
        # self.hp.switchto_parenttab()
        # time.sleep(2)
        # self.hp.click_twit()
        # self.hp.switchto_parenttab()
        # time.sleep(2)
        # self.hp.click_prestoweb()
        # self.hp.switchto_parenttab()
        self.hp.find_footer_ele()


