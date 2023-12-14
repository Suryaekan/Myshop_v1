import time

from PageObjects.Page_Women import PageWomen
from PageObjects.Product_page import Product
from testCases.conftest import setup
from utilities.readProperties import ReadConfig


class Test_womenpage:

    def test_wpage(self, setup):
        self.driver = setup
        url = ReadConfig.getapplicationurl()
        time.sleep(2)
        self.driver.get(url)
        self.driver.maximize_window()
        self.wp = PageWomen(self.driver)
        time.sleep(2)
        # self.driver.implicitly_wait(5)
        # self.wp.move_left_slider(60, 0)
        # time.sleep(2)
        # self.wp.move_right_slider(60, 0)

        # self.wp.click_quickview()

        self.wp.click_product()
        self.pp = Product(self.driver)
        self.pp.switch_productframe()
        self.pp.set_quantity(4)
        self.pp.increase_quantity()
        self.pp.decrease_quantity()
        self.pp.click_s_m_l("S")
        self.pp.click_s_m_l("L")
        self.pp.click_s_m_l("M")
        self.pp.click_white()
        self.pp.click_black()
        # time.sleep(1)
        self.pp.add_to_cart()
        time.sleep(4)
        # self.pp.continue_shopping()
        self.wp.click_product2()
        time.sleep(1)
        self.pp.switch_productframe()
        self.pp.click_s_m_l("L")
        self.pp.color_blue()
        self.pp.color_orange()
        self.pp.add_to_cart()
        self.pp.checkout()
