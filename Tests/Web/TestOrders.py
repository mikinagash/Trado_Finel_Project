from Base.base import Base
from selenium.webdriver.common.by import By

from Locators.LOrders2 import OrdersElement
from Utils.Utils import Utils
from time import sleep
from Pages.POrders2 import OrdersPage
import pytest
@pytest.mark.usefixtures('set_up')
class TestOrders(Base):


    @pytest.mark.regression
    def test_search_order_correct_by_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("עדי")
        # print(len(OrdersElement.table))
        # a.validtion( len(OrdersElement.table > 1),len(OrdersElement.table > 1))

    def test_search_order_correct_by_partly_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("עד")


    def test_search_order_incorrect_with_special_characters(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("!#$%&")

    def test_search_order_incorrect_by_first_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גגג")
        asrt = self.driver.find_element(By.XPATH, OrdersElement.error_msg).text
        a.validtion(asrt,"מציג \n לעמוד\nאין תוצאות\nסה״כ: 0 שורות","pic")
        print(asrt)






    def test_downloud_order_file(self):
        driver = self.driver
        a = Utils(driver)
        file = OrdersPage(driver)
        file.downloud_file()




    def test_search_order_correct_by_last_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גרובר")
        sleep(3)




    def test_search_order_incorrect_by_last_name(self):
        driver = self.driver
        a = Utils(driver)
        search = OrdersPage(driver)
        search.enter_order("גגג")


    def test_verify_user_can_order_details(self):
        driver = self.driver
        a = Utils(driver)
        order = OrdersPage(driver)
        order.select_order()


    def test_verify_user_can_export_of_rady_order(self):
        driver = self.driver
        downloud = OrdersPage(driver)
        downloud.export_files_Redy_order()


















