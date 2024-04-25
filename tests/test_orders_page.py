import allure
from Diplom_3.pages.orders_page import OrdersPage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.header_page import HeaderPage
from Diplom_3.pages.user_account_page import UserAccountPage
from Diplom_3.conftest import driver, login, create_and_delete_user


class TestOrderListPage:
    @allure.title('Проверка всплывающего окна с деталями заказа')
    def test_open_order_details_popup(self, driver):
        orders_page = OrdersPage(driver)
        HeaderPage(driver).click_orders_list_btn()
        orders_page.click_order()
        assert orders_page.check_order_structure_title().is_displayed()

    @allure.title('Проверка отображения созданного заказа в Ленте заказов')
    def test_new_order_in_orderlist(self, driver, login):
        orders_page = OrdersPage(driver)
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        account_page = UserAccountPage(driver)
        main_page.make_order_and_get_order_number()
        account_page.click_account_btn()
        account_page.click_on_order_list()
        account_page.find_order_status()
        order_number = account_page.get_order_number()
        header_page.click_orders_list_btn()
        orders_page.find_orders_list_title()
        wanted_order = orders_page.get_order_in_orderlist(order_number)
        assert wanted_order.is_displayed()

    @allure.title('Проверка изменения счетчика "Выполнено за все время" после создания заказа')
    def test_change_counter_total_orders(self, driver, login):
        orders_page = OrdersPage(driver)
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.find_ingredient_bun()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_order_list_title()
        total_number = orders_page.get_total_orders_number()
        header_page.click_constructor_btn()
        main_page.wait_visibility_burger_constructor_title()
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_order_list_title()
        new_total_number = orders_page.get_total_orders_number()
        assert int(new_total_number) == int(total_number) + 1

    @allure.title('Проверка изменения счетчика "Выполнено за сегодня" после создания заказа')
    def test_change_counter_today_orders(self, driver, login):
        orders_page = OrdersPage(driver)
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        main_page.find_ingredient_bun()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_order_list_title()
        today_number = orders_page.get_today_orders_number()
        header_page.click_constructor_btn()
        main_page.wait_visibility_burger_constructor_title()
        main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_order_list_title()
        new_number = orders_page.get_today_orders_number()
        assert int(new_number) == int(today_number) + 1

    @allure.title('Проверка отображения нового заказа в списке "В работе"')
    def test_new_order_appears_in_work_list(self, driver, login):
        orders_page = OrdersPage(driver)
        main_page = MainPage(driver)
        header_page = HeaderPage(driver)
        new_order = main_page.make_order_and_get_order_number()
        header_page.click_orders_list_btn()
        orders_page.wait_visibility_all_orders_ready()
        orders_page.wait_visibility_order_in_work()
        order_in_work = orders_page.get_order_number_in_work()
        assert new_order in order_in_work
