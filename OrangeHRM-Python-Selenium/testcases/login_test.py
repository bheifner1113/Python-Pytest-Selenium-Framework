from operator import truediv
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestLoginPage:
    
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    invalidUsername = ReadConfig.getInvalidUsername()
    invalidPassword = ReadConfig.getInvalidPassword()
    logger = LogGen.loggen()



    def test_login_Success(self): 
        self.lp = LoginPage(self.driver)
        self.logger.info("***********logging stuff here***************")
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_Success.png")
            assert False
    

    def test_login_correctUsernameWrongPassword(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.invalidPassword)
        self.lp.clickLogin()
        if self.lp.loginErrorText() == "Invalid credentials":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_correctUsernameWrongPassword.png")
            assert False


    def test_login_wrongUsernameWrongPassword(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.invalidUsername)
        self.lp.setPassword(self.invalidPassword)
        self.lp.clickLogin()
        if self.lp.loginErrorText() == "Invalid credentials":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_wrongUsernameWrongPassword.png")
            assert False

    def test_login_usernameOnly(self):
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.clickLogin()
        if self.lp.loginErrorText() == "Password cannot be empty":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_usernameOnly.png")
            assert False        

    def test_login_passwordOnly(self):
        self.lp = LoginPage(self.driver)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.lp.loginErrorText() == "Username cannot be empty":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login_passwordOnly.png")
            assert False    