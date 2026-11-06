import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import UrbanRoutesPage
import helpers


class TestUrbanRoutes:
    driver = None
    routes_page = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        self.routes_page.set_from(data.ADDRESS_FROM)
        self.routes_page.set_to(data.ADDRESS_TO)
        self.routes_page.click_call_taxi()
        assert self.routes_page.driver.find_element(*self.routes_page.from_field).get_property(
            'value') == data.ADDRESS_FROM
        assert self.routes_page.driver.find_element(*self.routes_page.to_field).get_property('value') == data.ADDRESS_TO

    def test_select_plan(self):
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.get_selected_plan() == "Comfort"

    def test_fill_phone_number(self):
        self.routes_page.set_phone(data.PHONE_NUMBER)
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.routes_page.set_code(phone_code)

        assert data.PHONE_NUMBER.replace(" ", "") in (
            self.routes_page.get_registered_phone().replace(" ", "")
        )

    def test_fill_card(self):
        self.routes_page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.routes_page.get_payment_method() == "Cartão"

    def test_comment_for_driver(self):
        self.routes_page.set_comment(data.MESSAGE_FOR_DRIVER)
        assert self.routes_page.driver.find_element(*self.routes_page.message_field).get_property(
            'value') == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.routes_page.order_blanket_and_handkerchiefs()
        assert self.routes_page.driver.find_element(*self.routes_page.blanket_checkbox).is_selected()

    def test_order_2_ice_creams(self):
        self.routes_page.order_2_ice_creams()
        ice_cream_count = self.routes_page.driver.find_element(*self.routes_page.ice_cream_value).text
        assert ice_cream_count == '2'

    def test_car_search_model_appears(self):
        self.routes_page.click_final_order()
        assert self.routes_page.is_car_search_modal_visible()