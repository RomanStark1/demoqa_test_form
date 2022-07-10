from selene.support.shared import browser

'''функция при помощи которой можно скрыть элементы мешающие тесту'''
def remove_element(elem):
    scr = f"$('{elem}').remove();"
    return browser.execute_script(scr)