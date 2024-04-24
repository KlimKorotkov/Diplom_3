import allure
from Diplom_3.locators.header_locators import HeaderLocators
from Diplom_3.locators.orders_page_locators import OrdersPageLocators
from Diplom_3.pages.base_page import BasePage


class HeaderPage(BasePage):
    @allure.step('Клик по кнопке "Лента заказов"')
    def click_orders_list_btn(self):
        self.move_to_element_and_click(HeaderLocators.ORDERS_LIST_BTN)
        self.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_btn(self):
        self.click_to_visible_element(HeaderLocators.CONSTRUCTOR_BTN)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_user_account_btn(self):
        self.move_to_element_and_click(HeaderLocators.ACCOUNT_BTN)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_order_list_title(self):
        self.driver.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)
