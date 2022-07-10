from selene.support.shared import browser


def select_dropdown(element, option):
    return browser.element(element).type(option).press_tab()