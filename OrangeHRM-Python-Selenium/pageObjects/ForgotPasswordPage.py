from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

class ForgotPasswordPage:
    cancel_button_id = "btnCancel"
    resetPasswordUsername_textField_id = "securityAuthentication_userName"
    resetPasswordButton_id = "btnSearchValues"
    warningMessage_css = ".message.warning.fadable"
    


    def __init__(self,driver):
        self.driver = driver


    def setResetPasswordUsername(self,username):
        self.driver.find_element(By.ID, self.resetPasswordUsername_textField_id).clear()
        self.driver.find_element(By.ID, self.resetPasswordUsername_textField_id).send_keys(username)

    def clickCancelButton(self):
        self.driver.find_element(By.ID, self.cancel_button_id).click()

    def clickResetPasswordButton(self):
        self.driver.find_element(By.ID, self.resetPasswordButton_id).click()

    def warningMessage(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.warningMessage_css).text
