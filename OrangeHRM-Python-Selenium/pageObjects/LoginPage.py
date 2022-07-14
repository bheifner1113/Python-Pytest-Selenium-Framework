from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

class LoginPage:
    username_textbox_id = "txtUsername"
    password_textbox_id = "txtPassword"
    login_button_id = "btnLogin"
    loginErrorText_id = "spanMessage"
    forgotPassword_link_css = "#forgotPasswordLink a"
    loginPanelHeading_id = "logInPanelHeading"

    #self.driver.find_element(By.ID, "spanMessage").text


    def __init__(self,driver):
        self.driver = driver


    def setUsername(self,username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def loginErrorText(self):
        return self.driver.find_element(By.ID, self.loginErrorText_id).text

    def clickForgotPasswordLink(self):
        self.driver.find_element(By.CSS_SELECTOR, self.forgotPassword_link_css).click()

    def loginPanelHeading(self):
        return self.driver.find_element(By.ID, self.loginPanelHeading_id).text