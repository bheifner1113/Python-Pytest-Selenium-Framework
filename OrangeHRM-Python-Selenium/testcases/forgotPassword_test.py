import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.ForgotPasswordPage import ForgotPasswordPage


@pytest.mark.usefixtures("setup")
class TestForgotPassword:
    
    def test_cancelForgotPassword(self): 
        self.lp = LoginPage(self.driver)
        self.fp = ForgotPasswordPage(self.driver)
        self.lp.clickForgotPasswordLink()
        self.fp.clickCancelButton()
        if self.lp.loginPanelHeading() == "LOGIN Panel":
            assert True   
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_forgotPassword_test_cancelForgotPassword.png")
            assert False


    def test_resetPassword(self):
        self.lp = LoginPage(self.driver)
        self.fp = ForgotPasswordPage(self.driver)
        self.lp.clickForgotPasswordLink()
        self.fp.setResetPasswordUsername("Admin")
        self.fp.clickResetPasswordButton()
        #print(self.fp.warningMessage())
        if self.fp.warningMessage() == "There is a password reset request already in the system.\nClose":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_forgotPassword_test_resetPassword.png")
            assert False
        