from selenium.webdriver.common.by import By


class HomePage:
    """

    Locators and methods for Home page.

    """
    CARD_LINK_TO_EVENTS_XPATH ="//div[@class='MuiCardMedia-root']/a"
    KEYWORD_INPUT_XPATH = "//input[@name = 'keyWord']"
    MORE_FILTERS_BUTTON_XPATH = "//span[contains(text(), 'more filters...')]"
    DATA_FROM_INPUT_XPATH = "//div[@class='MuiFormControl-root MuiTextField-root']/label[text()='From']/following-sibling::div/input"
    DATA_TO_INPUT_XPATH = "//div[@class='MuiFormControl-root MuiTextField-root']/label[text()='To']/following-sibling::div/input"
    HASHTAGS_INPUT_XPATH = "//input[@role = 'listbox']"
    FILTER_BY_LOCATION_BUTTON_XPATH = "//span[text() = 'Filter by location']"
    LESS_BUTTON_XPATH = "//span[text() = 'less...']"
    RESET_BUTTON_XPATH = "//span[contains(text(), 'Reset')]"
    FAVORITE_BUTTON_XPATH = "//span[contains(text(), 'Favorite')]"
    SEARCH_BUTTON_XPATH = "//span[contains(text(), 'Search')]"

    def __init__(self, driver):
        self.driver = driver

    def click_link_to_event(self, index):
        self.driver.find_elements(By.XPATH, self.CARD_LINK_TO_EVENTS_XPATH)[index].click()

    def get_pagination(self, number_of_page):
        return f"//div/button[@class='btn btn-primary'][{number_of_page}]"

    def pagination(self, index):
        self.driver.find_element(By.XPATH, self.get_pagination(index)).click()

    def send_keyword_input(self, string):
        self.driver.find_element(By.XPATH, self.KEYWORD_INPUT_XPATH).send_keys(string)

    def click_more_filters(self):
        self.driver.find_element(By.XPATH, self.MORE_FILTERS_BUTTON_XPATH).click()

    def data_input_from(self, data):
        self.driver.find_element(By.XPATH, self.DATA_FROM_INPUT_XPATH).send_keys(data)

    def data_input_to(self, data):
        self.driver.find_element(By.XPATH, self.DATA_TO_INPUT_XPATH).send_keys(data)

    def send_hashtags_input(self, string):
        self.driver.find_element(By.XPATH, self.HASHTAGS_INPUT_XPATH).send_keys(string)

    def get_checkboxes(self, number_of_checkbox):
        return f"//input[@name = 'statuses[{number_of_checkbox}]']"

    def click_checkbox(self, active_blocked_canceled):
        self.driver.find_element(By.XPATH, self.get_checkboxes(active_blocked_canceled)).click()

    def click_filter_by_location(self):
        self.driver.find_element(By.XPATH, self.FILTER_BY_LOCATION_BUTTON_XPATH).click()

    def click_less(self):
        self.driver.find_element(By.XPATH, self.LESS_BUTTON_XPATH).click()

    def click_reset(self):
        self.driver.find_element(By.XPATH, self.RESET_BUTTON_XPATH).click()

    def click_favorite(self):
        self.driver.find_element(By.XPATH, self.FAVORITE_BUTTON_XPATH).click()

    def click_search(self):
        self.driver.find_element(By.XPATH, self.SEARCH_BUTTON_XPATH).click()
