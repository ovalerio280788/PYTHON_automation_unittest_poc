__author__ = 'Oscar Mario'


class PageFactory:

    def init_elements(self, driver, class_page):
        new_p = class_page
        variables = tuple(set(dir(new_p)))

        for var in variables:
            if "Find_" in var:
                var_value = getattr(new_p, var)
                web_element = self.find_element(driver, var_value[0], var_value[1])
                setattr(new_p, var, web_element)
        return new_p

    def find_element(self, driver, selector_type, selector_value):
        if selector_type == "xpath":
            return driver.find_element_by_xpath(selector_value)
        elif selector_type == "css selector":
            return driver.find_element_by_css_selector(selector_value)
