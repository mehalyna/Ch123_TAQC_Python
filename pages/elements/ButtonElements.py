from pages.common.baseContext import BaseContext


class ButtonElements(BaseContext):
    """
        Class for click on Button by text button.
    """
    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def click_btn_by_name(self, btn_name):
        """
            Method for click on a needed button by text button and css selector.
        """
        elements = self.find_elements(self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return
