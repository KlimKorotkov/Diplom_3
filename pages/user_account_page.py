import allure
from Diplom_3.locators.user_account_locators import UserAccountLocators
from Diplom_3.pages.base_page import BasePage


class UserAccountPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_password_recover_btn(self):
        self.click_to_visible_element(UserAccountLocators.RESET_PASSWORD_BTN)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_account_btn(self):
        self.move_to_element_and_click(UserAccountLocators.ACCOUNT_BTN)
        self.wait_visibility_element(UserAccountLocators.PROFILE_BTN)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_btn(self):
        self.click_to_visible_element(UserAccountLocators.EXIT_BTN)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_list(self):
        self.click_to_visible_element(UserAccountLocators.ORDERS_HISTORY_BTN)

    @allure.step('Получение номера заказа в "История заказов"')
    def get_order_number(self):
        return self.get_text_of_element(UserAccountLocators.ORDER_NUMBER)

    @allure.step('Авторизация пользователя')
    def login(self, email, password):
        self.driver.set_text_to_element(UserAccountLocators.INPUT_EMAIL, email)
        self.driver.set_text_to_element(UserAccountLocators.INPUT_PASSWORD, password)
        self.driver.click_to_visible_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Поиск элемента')
    def find_order_status(self):
        return self.driver.find_element(UserAccountLocators.ORDER_STATUS)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_profile_btn(self):
        self.driver.find_element(UserAccountLocators.PROFILE_BTN)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_enter_btn(self):
        self.driver.find_element(UserAccountLocators.ENTER_BTN)

    @allure.step('Получение текста элемента')
    def get_text_of_enter_btn(self):
        return self.driver.find_element(UserAccountLocators.ENTER_BTN).text
