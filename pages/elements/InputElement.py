from pages.common.baseWrapper import BaseWrapper


class InputElement(BaseWrapper):
    """
        Class for sending data to input field.
    """
    def __init__(self, selector, driver):
        """
            Method for class fields declaration.
        """
        super().__init__(driver)
        self.selector = selector

    def send_data(self, string):
        """
        Method for sending data to input field.
        :param string: Variable string should contain text which we need to enter.
        """
        self.find_element_by_css(self.selector).send_keys(string)

