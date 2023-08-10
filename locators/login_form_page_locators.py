from selenium.webdriver.common.by import By


class LoginFormPageLocators:
    # input
    USER_NAME_INPUT =(By.CSS_SELECTOR,'input[id="user-name"]')
    PASSWORD_INPUT =(By.CSS_SELECTOR,'input[id="password"]')
    # button
    LOGIN_BUTTON =(By.CSS_SELECTOR,'input[id="login-button"]')
    # date
    USER_NAME =(By.CSS_SELECTOR,'div[id="login_credentials"]')
    PASSWORD = (By.CSS_SELECTOR,'div[class="login_password"]')
    # error
    ERROR_BUTTON = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')