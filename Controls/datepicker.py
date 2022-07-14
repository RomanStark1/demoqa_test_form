from selene.core.entity import Element
from selene.support.shared.jquery_style import s


class Datepicker:

    def __init__(self, element: Element):
        self.element = element

    def choose_date(self, year: str, month: str, day: str):
        self.element.click()
        s('.react-datepicker__year-select').s(f'[value="{year}"]').click()
        s('.react-datepicker__month-select').s(f'[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}').click()