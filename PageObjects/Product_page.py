import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from testCases.conftest import setup


class Product:
    txt_quantity_xpath = "//input[@id='quantity_wanted']"
    btn_quantitydecrease_xpath = "//i[@class='icon-minus']"
    btn_quantityincrease_xpath = "//i[@class='icon-plus']"
    drp_size_xpath = "//select[@id='group_1']"
    frame_productview_tag = "iframe"
    btn_color_white = "#color_8"
    btn_color_black = "#color_11"

    btn_addtocart_xpath = "//span[normalize-space()='Add to cart']"

    img_enlarge_xpath = "//img[@id='bigpic']"
    img_movenext_xpath = "//a[@title='Next']"
    img_moveprevious_xpath = "//a[@title='Previous']"

    btn_continueshopping_xpath = "//span[@title='Continue shopping']//span[1]"
    btn_color_orange = "#color_13"
    btn_color_blue = "# color_14"
    btn_checkout_xpath = "//span[normalize-space()='Proceed to checkout']"

    def __init__(self, setup):
        self.driver = setup

    def set_quantity(self, quantity):
        quan = self.driver.find_element(By.XPATH, self.txt_quantity_xpath)
        quan.clear()
        quan.send_keys(quantity)

    def increase_quantity(self):
        self.driver.find_element(By.XPATH, self.btn_quantityincrease_xpath).click()

    def decrease_quantity(self):
        self.driver.find_element(By.XPATH, self.btn_quantitydecrease_xpath).click()

    def click_size(self):
        size = self.driver.find_element(By.XPATH, self.drp_size_xpath)
        select = Select(size)
        return select

    def click_s_m_l(self, size):
        select = self.click_size()
        select.select_by_visible_text(size)

    def switch_productframe(self):
        frame = self.driver.find_element(By.TAG_NAME, self.frame_productview_tag)
        self.driver.switch_to.frame(frame)

    def click_white(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_color_white).click()

    def click_black(self):
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_color_black).click()

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.btn_addtocart_xpath).click()

    def continue_shopping(self):
        self.driver.find_element(By.XPATH, self.btn_continueshopping_xpath).click()

    def color_orange(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_color_orange).click()

    def color_blue(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_color_orange).click()

    def checkout(self):
        self.driver.find_element(By.XPATH, self.btn_checkout_xpath).click()




