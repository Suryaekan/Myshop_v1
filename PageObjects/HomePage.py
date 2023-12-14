from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    title = "My Shop"
    btn_homepage_xpath = "//img[@alt='My Shop']"
    btn_signin_lnk = "Sign in"
    btn_contact_lnk = "Contact us"
    txt_emailcreate_xpath = "//input[@id='email_create']"
    btn_createacc_css = "button[id='SubmitCreate'] span"
    txt_search_xpath = "//input[@id='search_query_top']"
    btn_search_xpath = "//button[@name='submit_search']"
    btn_cart_css = "a[title='View my shopping cart']"
    btn_women_xpath = "//a[@title='Women']"
    btn_dresses_xpath = ("//body/div[@id='page']/div[@class='header-container']/header[@id='header']/div/div["
                         "@class='container']/div[@class='row']/div[@id='block_top_menu']/ul[@class='sf-menu"
                         " clearfix menu-content sf-js-enabled sf-arrows']/li[2]/a[1]")
    btn_blog_xpath = "//a[@title='Blog']"

    btn_tshirts_xpath = "//li[@class='sfHover']//a[@title='T-shirts'][normalize-space()='T-shirts']"
    lnk_tops_xpath = "//a[@title='Tops']"
    lnk_tshirts_xpath = "//ul[@class='menu-mobile clearfix']//ul//li//a[@title='T-shirts'][normalize-space()='T-shirts']"
    lnk_dresses_xpath = "//ul[@class='menu-mobile clearfix']//a[@title='Dresses'][normalize-space()='Dresses']"
    lnk_casual_dresses = "//ul[@class='menu-mobile clearfix']//ul//li//a[@title='Casual Dresses'][normalize-space()='Casual Dresses']"
    lnk_evening_dresses = "//ul[@class='menu-mobile clearfix']//ul//li//a[@title='Evening Dresses'][normalize-space()='Evening Dresses']"
    lnk_summer_dresses = "//ul[@class='menu-mobile clearfix']//ul//li//a[@title='Summer Dresses'][normalize-space()='Summer Dresses']"

    lnk_casual_dresses2 = "//li[@class='sfHover']//a[@title='Casual Dresses'][normalize-space()='Casual Dresses']"
    lnk_evening_dresses2 = "//li[@class='sfHover']//a[@title='Evening Dresses'][normalize-space()='Evening Dresses']"
    lnk_summer_dresses2 = "//li[@class='sfHover']//a[@title='Summer Dresses'][normalize-space()='Summer Dresses']"

    lnk_blouses_xpath = "//a[@title='Blouses']"

    slider_1 = "(//div[@class='homeslider-description'])[4]"

    lnk_img1_xpath = "//div[@id='htmlcontent_top']//li[@class='htmlcontent-item-1 col-xs-4']//img[@class='item-img ']"
    lnk_img2_xpath = "//div[@id='htmlcontent_top']//li[@class='htmlcontent-item-2 col-xs-4']//img[@class='item-img ']"
    lnk_img3_xpath = "(//img[@class='item-img '])[3]"
    lnk_img4_xpath = "(//img[@class='item-img '])[4]"
    lnk_img5_xpath = "(//img[@class='item-img '])[5]"
    lnk_img6_xpath = "(//img[@class='item-img '])[6]"
    lnk_img7_xpath = "(//img[@class='item-img '])[7]"


    lnk_bestsellers_xpath = "//a[normalize-space()='Best Sellers']"
    lnk_popular_xpath = "//a[normalize-space()='Popular']"

    txt_newsletter_xpath = "//input[@id='newsletter-input']"
    lnk_fb_xpath = "//a[@href='http://www.facebook.com/prestashop']"
    lnk_twit_xpath = "//a[@href='http://www.twitter.com/prestashop']"
    lnk_prestoweb_xpath = "//a[@href='http://www.prestashop.com/blog/en/feed/']"
    tag_footer_xpath = "//footer[@id='footer']//div[@class='row']"


    def __init__(self, driver):
        self.driver = driver

    def check_title(self):
        assert self.driver.title == self.title
        print("Title: "+self.driver.title)

    def click_sign_in(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_signin_lnk).click()

    def click_contact(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_contact_lnk).click()

    def click_women(self):
        self.driver.find_element(By.XPATH, self.btn_women_xpath).click()

    def hover_women(self):
        btn_women = self.driver.find_element(By.XPATH, self.btn_women_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_women).perform()

    def click_tops(self):
        self.hover_women()
        self.driver.find_element(By.XPATH, self.lnk_tops_xpath).click()

    def click_blouses(self):
        self.hover_women()
        self.driver.find_element(By.XPATH, self.lnk_blouses_xpath).click()

    def click_dresses(self):
        self.hover_women()
        self.driver.find_element(By.XPATH, self.lnk_dresses_xpath)

    def click_casual_dresses_women(self):
        self.hover_women()
        self.driver.find_element(By.XPATH, self.lnk_casual_dresses).click()

    def click_evening_dresses_women(self):
        self.hover_women()
        self.driver.find_element(By.XPATH, self.lnk_evening_dresses).click()

    def click_summer_dresses_women(self):
        self.hover_women()
        self.driver.find_element(By.XPATH, self.lnk_summer_dresses).click()

    def hover_dresses_btn(self):
        btn_dresses = self.driver.find_element(By.XPATH, self.btn_dresses_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_dresses).perform()

    def click_dresses_btn(self):
        self.driver.find_element(By.XPATH, self.btn_dresses_xpath).click()

    def click_casualdresses_2(self):
        self.hover_dresses_btn()
        self.driver.find_element(By.XPATH, self.lnk_casual_dresses2).click()

    def click_eveningdresses_2(self):
        self.hover_dresses_btn()
        self.driver.find_element(By.XPATH, self.lnk_evening_dresses2).click()

    def click_summerdresses_2(self):
        self.hover_dresses_btn()
        self.driver.find_element(By.XPATH, self.lnk_summer_dresses2).click()

    def click_blog_button(self):
        self.driver.find_element(By.XPATH, self.btn_blog_xpath).click()

    def click_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btn_cart_css).click()

    def clickslider(self,):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.slider_1).click()

    def click_home(self):
        self.driver.find_element(By.XPATH, self.btn_homepage_xpath).click()

    def click_imglnk_1(self):
        self.driver.find_element(By.XPATH, self.lnk_img1_xpath).click()

    def previous_page(self):
        self.driver.back()

    def click_imglnk_2(self):
        self.driver.find_element(By.XPATH, self.lnk_img2_xpath).click()

    def click_imglnk_3(self):
        self.driver.find_element(By.XPATH, self.lnk_img3_xpath).click()

    def click_imglnk_4(self):
        self.driver.find_element(By.XPATH, self.lnk_img4_xpath).click()

    def click_imglnk_5(self):
            self.driver.find_element(By.XPATH, self.lnk_img5_xpath).click()

    def click_imglnk_6(self):
        self.driver.find_element(By.XPATH, self.lnk_img6_xpath).click()

    def click_imglnk_7(self):
        self.driver.find_element(By.XPATH, self.lnk_img7_xpath).click()

    def subscribe_newsletter(self, mail):
        self.driver.find_element(By.XPATH, self.txt_newsletter_xpath).send_keys(mail)

    def click_fb(self):
        self.driver.find_element(By.XPATH, self.lnk_fb_xpath).click()

    def switchto_parenttab(self):
        parenthandle = self.driver.window_handles[0]
        self.driver.switch_to.window(parenthandle)

    def click_twit(self):
        self.driver.find_element(By.XPATH, self.lnk_twit_xpath).click()

    def click_prestoweb(self):
        self.driver.find_element(By.XPATH, self.lnk_prestoweb_xpath).click()

    # def find_footer_ele(self):
    #     list footer_elements = self.driver.find_elements(By.XPATH, self.tag_footer_xpath)
    #     print(footer_elements)
