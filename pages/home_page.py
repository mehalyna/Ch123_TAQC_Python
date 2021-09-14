from selenium.webdriver.common.by import By


class HomePage:
    """
    Locators and methods for Home page.
    """
    CARD_LINK_TO_EVENTS_XPATH ="//div[@class='MuiCardMedia-root']/a"
    KEYWORD_INPUT_CSS = "form > div:nth-child(1) > div > div > input"
    MORE_FILTERS_BUTTON_CSS = "div:nth-child(2) > button > span.MuiButton-label"
    DATA_FROM_INPUT_CSS = "form > div:nth-child(2) > div > div > input"
    DATA_TO_INPUT_CSS = "form > div:nth-child(3) > div > div > input"
    HASHTAGS_INPUT_CSS = "div:nth-child(4) > div > div > div > input"
    FILTER_BY_LOCATION_BUTTON_CSS = "div:nth-child(6) > div > button > span.MuiButton-label"
    LESS_BUTTON_CSS = "div:nth-child(8) > button > span.MuiButton-label"
    RESET_BUTTON_CSS = "div.d-flex > button:nth-child(1) > span.MuiButton-label"
    FAVORITE_BUTTON_CSS = "div.d-flex > button:nth-child(2) > span.MuiButton-label"
    SEARCH_BUTTON_CSS = "div.d-flex > button:nth-child(3) > span.MuiButton-label"

    def __init__(self, driver):
        self.driver = driver

    def click_link_to_event(self, index):
        self.driver.find_elements(By.XPATH, self.CARD_LINK_TO_EVENTS_XPATH)[index].click()

    def get_pagination(self, number_of_page):
        return f"ul > div > div > button:nth-child({number_of_page})"

    def click_page_btn(self, index):
        self.driver.find_element(By.CSS_SELECTOR, self.get_pagination(index)).click()

    def send_keyword_input(self, string):
        self.driver.find_element(By.CSS_SELECTOR, self.KEYWORD_INPUT_CSS).send_keys(string)

    def click_more_filters_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.MORE_FILTERS_BUTTON_CSS).click()

    def send_data_from_input(self, data):
        self.driver.find_element(By.CSS_SELECTOR, self.DATA_FROM_INPUT_CSS).send_keys(data)

    def send_data_to_input(self, data):
        self.driver.find_element(By.CSS_SELECTOR, self.DATA_TO_INPUT_CSS).send_keys(data)

    def send_hashtags_input(self, string):
        self.driver.find_element(By.CSS_SELECTOR, self.HASHTAGS_INPUT_CSS).send_keys(string)

    def get_checkboxes(self, number_of_checkbox):
        return f"div:nth-child({number_of_checkbox}) > label > input[type=checkbox]"

    def click_checkbox(self, active_blocked_canceled):
        self.driver.find_element(By.CSS_SELECTOR, self.get_checkboxes(active_blocked_canceled)).click()

    def click_filter_by_location_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.FILTER_BY_LOCATION_BUTTON_CSS).click()

    def click_less_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.LESS_BUTTON_CSS).click()

    def click_reset_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.RESET_BUTTON_CSS).click()

    def click_favorite_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.FAVORITE_BUTTON_CSS).click()

    def click_search_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_BUTTON_CSS).click()
