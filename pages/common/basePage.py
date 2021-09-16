from pages.common.baseContext import BaseContext


class BasePage(BaseContext):
    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        super().__init__(driver)
        self.base_url = "https://eventsexpress-test.azurewebsites.net/"

    def go_to_site(self):
        """
            Method for go to the base_url
        """
        return self.driver.get(self.base_url)
