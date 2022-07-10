from selene.support.shared import browser


def cells_of_row(number):
    return browser.element(f'//*[@class="table-responsive"]//tr[{number}]//td[2]')