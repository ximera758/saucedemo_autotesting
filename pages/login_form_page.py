from pages.base_page import BasePage
from locators.login_form_page_locators import LoginFormPageLocators


class LoginFormPage(BasePage):
    locators = LoginFormPageLocators

    def check_name_presence(self):
        all_names = self.element_are_presence(self.locators.USER_NAME)
        return all_names[0].text

    def check_password_presence(self):
        password = self.element_are_presence(self.locators.PASSWORD)
        return password[0].text

    def check_login_with_standard_user(self):
        self.element_are_visible(self.locators.USER_NAME_INPUT).click()
        self.element_are_visible(self.locators.USER_NAME_INPUT).send_keys('standard_user')
        self.element_are_visible(self.locators.PASSWORD_INPUT).send_keys('secret_sauce')
        self.element_are_visible(self.locators.LOGIN_BUTTON).click()

    def check_login_with_locked_out_user(self):
        self.element_are_visible(self.locators.USER_NAME_INPUT).click()
        self.element_are_visible(self.locators.USER_NAME_INPUT).send_keys('locked_out_user')
        self.element_are_visible(self.locators.PASSWORD_INPUT).send_keys('secret_sauce')
        self.element_are_visible(self.locators.LOGIN_BUTTON).click()
        message = self.element_are_presence(self.locators.ERROR_BUTTON)
        return message[0].text

