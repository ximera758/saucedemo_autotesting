from pages.base_page import BasePage
from pages.login_form_page import LoginFormPage
from selenium import webdriver
import time

class TestLoginForm:

    def test_name_presence(self, driver):
        test_login_page = LoginFormPage(driver, 'https://www.saucedemo.com/')
        test_login_page.open()
        all_names = test_login_page.check_name_presence()
        real_name, invalid_name = 'standard_user', 'problem_user'
        assert real_name in all_names,'Real login not in all_logins!'
        assert invalid_name in all_names,'Real login not in all_logins!'

    def test_password_presence(self, driver):
        test_login_page = LoginFormPage(driver, 'https://www.saucedemo.com/')
        test_login_page.open()
        get_password = test_login_page.check_password_presence()
        password = 'secret_sauce'
        assert password in get_password,'Password not in get password!'


    def test_login_standart_user(self,driver):
        test_login_page = LoginFormPage(driver, 'https://www.saucedemo.com/')
        test_login_page.open()
        test_login_page.check_login_with_standard_user()
        assert True, 'Registration Error!'

    def test_login_problem_user(self,driver):
        test_login_page = LoginFormPage(driver, 'https://www.saucedemo.com/')
        test_login_page.open()
        message = test_login_page.check_login_with_locked_out_user()
        assert message == 'Epic sadface: Sorry, this user has been locked out.', 'Something went wrong'
