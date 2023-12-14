import time

from PageObjects.Page_Women import PageWomen
from PageObjects.Product_page import Product
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestWomenPage:
    logger = LogGen.loggen()

    def test_wpage(self, setup):
        self.logger.info("*** Test_womenpage started ***")
        self.driver = setup
        self.driver.get("http://www.automationpractice.pl/index.php?id_category=3&controller=category")
        self.logger.info("Launching Application")
        self.driver.maximize_window()
        self.wp = PageWomen(self.driver)
        time.sleep(2)
        # self.driver.implicitly_wait(5)
        # self.wp.move_left_slider(60, 0)
        # time.sleep(2)
        # self.wp.move_right_slider(60, 0)

        # self.wp.click_quickview()

        self.logger.info("Click on a product")
        self.wp.click_product()
        self.pp = Product(self.driver)
        self.logger.info("Switching to frame 1")
        self.pp.switch_productframe()
        self.logger.info("Setting quantity to 4")
        self.pp.set_quantity(4)
        self.logger.info("Clicking quantity increase button")
        self.pp.increase_quantity()
        self.logger.info("Clicking quantity decrease button")
        self.pp.decrease_quantity()
        self.logger.info("choosing dropdown Small")
        self.pp.click_s_m_l("S")
        self.logger.info("choosing dropdown Large")
        self.pp.click_s_m_l("L")
        self.logger.info("choosing dropdown Medium")
        self.pp.click_s_m_l("M")
        self.logger.info("choosing color White")
        self.pp.click_white()
        self.logger.info("choosing color Black")
        self.pp.click_black()
        # time.sleep(1)
        self.logger.info("Clicking add to cart button")
        self.pp.add_to_cart()
        time.sleep(4)
        # self.pp.continue_shopping()
        self.logger.info("Clicking second product")
        self.wp.click_product2()
        time.sleep(1)
        self.logger.info("Switching to frame 1")
        self.pp.switch_productframe()
        self.logger.info("choosing dropdown Large")
        self.pp.click_s_m_l("L")
        self.logger.info("choosing color Blue")
        self.pp.color_blue()
        self.logger.info("choosing color Orange")
        self.pp.color_orange()
        self.logger.info("Clicking add to cart button")
        self.pp.add_to_cart()
        self.logger.info("Clicking checkout button")
        self.pp.checkout()
        self.logger.info("*** Test_womenpage Finished ***")
