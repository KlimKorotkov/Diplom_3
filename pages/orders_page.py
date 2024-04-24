import allure
from Diplom_3.locators.orders_page_locators import OrdersPageLocators
from Diplom_3.pages.base_page import BasePage


class OrdersPage(BasePage):
    @allure.step('Клик по заказу в списке Лента заказов')
    def click_order(self):
        self.click_to_visible_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Получение заказа по номеру в Ленте заказов')
    def get_order_in_orderlist(self, order):
        method, locator = OrdersPageLocators.ORDER_NUMBER
        locator = locator.format(order)
        return self.find_element((method, locator))

    @allure.step('Получение количества заказов выполненных за все время')
    def get_total_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TOTAL)

    @allure.step('Получение количества заказов выполненных за сегодня')
    def get_today_orders_number(self):
        return self.get_text_of_element(OrdersPageLocators.COMPLETED_ORDERS_TODAY)

    @allure.step('Получение заказа по номеру в разделе "В работе"')
    def get_order_number_in_work(self):
        return self.get_text_of_element(OrdersPageLocators.ORDER_IN_WORK)

    @allure.step('Проверка отображения элемента на странице')
    def check_order_structure_title(self):
        self.driver.check_element(OrdersPageLocators.ORDER_STRUCTURE_TITLE)
        return self.driver.find_element(OrdersPageLocators.ORDER_STRUCTURE_TITLE)

    @allure.step('Поиск элемента')
    def find_orders_list_title(self):
        return self.driver.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_order_list_title(self):
        self.driver.find_element(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_all_orders_ready(self):
        self.driver.find_element(OrdersPageLocators.ALL_ORDERS_READY)

    @allure.step('Ожидание видимости элемента на странице')
    def wait_visibility_order_in_work(self):
        self.driver.find_element(OrdersPageLocators.ORDER_IN_WORK)


