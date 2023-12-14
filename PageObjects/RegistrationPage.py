import os.path
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Login:
    txt_emailcreate_xpath = "//input[@id='email_create']"
    btn_createacc_css = "button[id='SubmitCreate'] span"
    btn_register_xpath = "//span[normalize-space()='Register']"
    txt_errorcount_css = "div[class='alert alert-danger'] p"
    txt1_errorcount_css = ".alert.alert-danger"
    radio_mr_css = "#id_gender1"
    radio_mrs_css = "#id_gender2"
    txt_fname_xpath = "//input[@id='customer_firstname']"
    txt_lname_xpath = "//input[@id='customer_lastname']"
    txt_mailid_xpath = "//input[@id='email']"
    txt_pwd_xpath = "//input[@id='passwd']"
    drp_date_xpath = "//select[@id='days']"
    drp_month_xpath = "//select[@id='months']"
    drp_year_xpath = "//select[@id='years']"
    chk_newsltr_xpath = "//input[@id='newsletter']"
    msg_error_xpath = "//li[contains(text(),'An account using this email address has already be')]"

    def __init__(self, driver):
        self.driver = driver

    def create_account(self, mail):
        self.driver.find_element(By.XPATH, self.txt_emailcreate_xpath).send_keys(mail)
        self.driver.find_element(By.CSS_SELECTOR, self.btn_createacc_css).click()
        time.sleep(2)
        # error = self.driver.find_element(By.XPATH, self.msg_error_xpath).text
        # print(error)

    def register_account(self, gender, fname, lname, pwd, date, month, year):
        time.sleep(2)
        male = self.driver.find_element(By.CSS_SELECTOR, self.radio_mr_css)
        female = self.driver.find_element(By.CSS_SELECTOR, self.radio_mrs_css)
        if gender == "male":
            male.click()
        elif gender == "female":
            female.click()
        self.driver.find_element(By.XPATH, self.txt_fname_xpath).send_keys(fname)
        self.driver.find_element(By.XPATH, self.txt_lname_xpath).send_keys(lname)
        self.driver.find_element(By.XPATH, self.txt_pwd_xpath).send_keys(pwd)

        date_drop = self.driver.find_element(By.XPATH, self.drp_date_xpath)
        selectdate = Select(date_drop)
        selectdate.select_by_value(date)

        month_drop = self.driver.find_element(By.XPATH, self.drp_month_xpath)
        select_month = Select(month_drop)
        select_month.select_by_value(month)

        year_drop = self.driver.find_element(By.XPATH, self.drp_year_xpath)
        select_year = Select(year_drop)
        select_year.select_by_value(year)

        self.driver.find_element(By.XPATH, self.chk_newsltr_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

        time.sleep(4)
        print("Registration successfull")
        self.driver.save_screenshot(os.path.abspath(os.curdir)+'\\screenshots\\'+'test_homepage.jpg')
        self.driver.quit()
