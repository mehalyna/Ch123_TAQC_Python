from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common.baseWrapper import BaseWrapper



class TableElement(BaseWrapper):

    def __init__(self, table_selector, driver):
        super().__init__(driver)
        self.table_selector = table_selector

    def find_element_in_row(self, search_name, wait_time = 10):
        """
            Method looks for text in a specific table and returns
            the row number in which the text is located
        :param search_name - text, that we need to find in table
        """
        elements = self.find_element_by_css(self.table_selector)
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.table_selector)))
        for idx, element in enumerate(elements):
            if element.text == search_name:
                return idx
