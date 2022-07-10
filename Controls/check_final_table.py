
from selene import have
from selene.support.shared import browser


class FinalTable:

    def __init__(self, row_num, result):
        self.row_num = row_num
        self.result = result

    def result_assert(self):
        browser.all('.table-responsive tbody tr')[self.row_num].all('td')[1].should(have.exact_text(self.result))