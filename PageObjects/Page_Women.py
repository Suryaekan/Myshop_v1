from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PageWomen:
    btn_women_xpath = "//a[@title='Women']"
    lnk_tops_xpath = "//div[@class='block_content']//a[normalize-space()='Tops']"
    drp_tops_xpath = "//div[@id='categories_block_left']//li[1]//span[1]"

    drp_dresses_xpath = "//div[@class='block_content']//li[@class='last']//span[@class='grower CLOSE']"
    lnk_dresses_xpath = "//div[@class='block_content']//a[contains(@title,'Find your favorites dresses from our wide choice of evening, casual or summer dresses!')][normalize-space()='Dresses']"
    lnk_tshirts_xpath = "//div[@class='block_content']//ul//a[contains(@title,'The must have of your wardrobe, take a look at our different colors,')][normalize-space()='T-shirts']"
    lnk_blouses_xpath = "//div[@class='block_content']//ul//a[@title='Match your favorites blouses with the right accessories for the perfect look.'][normalize-space()='Blouses']"

    lnk_casualdress_xpath = "//div[@class='block_content']//ul[@class='tree dynamized']//li[@class='last']//ul//li//a[contains(@title,'You are looking for a dress for every day? Take a look at')][normalize-space()='Casual Dresses']"
    lnk_eveningdresses_xpath = "//div[@class='block_content']//ul[@class='tree dynamized']//li[@class='last']//ul//li//a[@title='Browse our different dresses to choose the perfect dress for an unforgettable evening!'][normalize-space()='Evening Dresses']"
    lnk_summersresses_xpath = "//div[@class='block_content']//ul//a[@title='Short dress, long dress, silk dress, printed dress, you will find the perfect dress for summer.'][normalize-space()='Summer Dresses']"

    chk_tops_xpath = "//input[@id='layered_category_4']"
    chk_dresses_xpath = "//input[@id='layered_category_8']"

    chk_sizesmall_xpath = "//input[@id='layered_category_8']"
    chk_sizemedium_xpath = "//input[@id='layered_category_8']"
    chk_sizelarge_xpath = "//input[@id='layered_category_8']"

    drp_sort_xpath = "//select[@id='selectProductSort']"
    drp_priceasc_visibletxt = "Price: Lowest first"
    drp_pricedsc_visibletxt = "Price: Highest first"
    drp_nameasc_visibletxt = "Product Name: A to Z"
    drp_namedsc_visibletxt = "Product Name: Z to A"
    drp_instock_xpath = "//option[@value='quantity:desc']"

    btn_gridview_xpath = "//a[normalize-space()='Grid']"
    btn_listview_xpath = "//a[normalize-space()='List']"

    btn_beigecolour_xpath = "//ul[@id='ul_layered_id_attribute_group_3']//li[1]"
    btn_whitecolour_xpath = "//label[@name='layered_id_attribute_group_8']//span[1]"
    btn_blackcolour_xpath = "//label[@name='layered_id_attribute_group_11']//a[1]"
    btn_orangecolour_xpath = "//label[@name='layered_id_attribute_group_13']//a[1]"
    btn_bluecolour_xpath = "//label[@name='layered_id_attribute_group_14']//a[1]"
    btn_greencolour_xpath = "//label[@name='layered_id_attribute_group_15']//a[1]"
    btn_yellowcolour_xpath = "//label[@name='layered_id_attribute_group_16']//a[1]"
    btn_pinkcolour_xpath = "//label[@name='layered_id_attribute_group_24']//span[1]"

    chk_colourfuldresses_xpath = "//input[@id='layered_id_feature_18']"
    chk_maxifuldresses_xpath = "//input[@id='layered_id_feature_21']"
    chk_midifuldresses_xpath = "//input[@id='layered_id_feature_20']"
    chk_shortdresses_xpath = "//input[@id='layered_id_feature_19']"
    chk_shortsleeve_xpath = "//input[@id='layered_id_feature_17']"
    slider_left_xpath = "//div[@class='layered_price']//a[1]"
    slider_right_xpath = "//div[@class='layered_price']//a[2]"

    img_blouse_xpath = "//img[@title='Blouse']"
    hover_quickview_xpath = "//li[@class='ajax_block_product col-xs-12 col-sm-6 col-md-4 last-item-of-tablet-line hovered']//span[contains(text(),'Quick view')]"
    btn_addtocart_xpath = "(//span[contains(text(),'Add to cart')])[1]"
    img_product2_xpath = "//img[@title='Faded Short Sleeve T-shirts']"

    def __init__(self, driver):
        self.driver = driver

    def move_right_slider(self, xoffset_value, yoffset_value):
        slide1 = self.driver.find_element(By.XPATH, self.slider_left_xpath)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slide1, xoffset_value, yoffset_value).perform()

    def move_left_slider(self, xoffset_value, yoffset_value):
        slide2 = self.driver.find_element(By.XPATH, self.slider_right_xpath)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slide2, -xoffset_value, yoffset_value).perform()

    def click_product(self):
        self.driver.find_element(By.XPATH, self.img_blouse_xpath).click()

    def click_product2(self):
        self.driver.find_element(By.XPATH, self.img_product2_xpath).click()