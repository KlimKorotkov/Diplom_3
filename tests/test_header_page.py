import allure
from Diplom_3.locators.orders_page_locators import OrdersPageLocators
from Diplom_3.pages.header_page import HeaderPage
from Diplom_3.data import Urls
from Diplom_3.conftest import driver


class TestHeaderPage:
    def setup_class_header_page(self):
        self.header_page = HeaderPage(driver)

    @allure.title('Проверка перехода в "Конструктор"')
    def test_redirect_to_constructor(self):
        self.header_page.click_orders_list_btn()
        self.header_page.wait_visibility_element(OrdersPageLocators.ORDERS_LIST_TITLE)
        self.header_page.click_constructor_btn()
        current_url = self.header_page.get_current_url()
        assert current_url == Urls.MAIN_PAGE

    @allure.title('Проверка перехода в Ленту заказов')
    def test_redirect_to_order_list(self):
        self.header_page.click_orders_list_btn()
        current_url = self.header_page.get_current_url()
        assert current_url == Urls.FEED
