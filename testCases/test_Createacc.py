from PageObjects.RegistrationPage import Login
from testCases.conftest import setup
from PageObjects.RegistrationPage import Login


class Test_homepage:
    url_accountcreation = ("http://www.automationpractice.pl/index.php?controller="
                           "authentication&back=my-account#account-creation")

    def test_reg_page(self, setup):
        self.driver = setup
        self.driver.get(self.url_accountcreation)
        self.rp = Login(self.driver)

        self.rp = Login(self.driver)
        self.rp.create_account("xyz972@gmail.com")
        self.rp.register_account("male", "Surya", "V",
                               "123456!", "12", "10", "1980")
