from selene.support.shared.jquery_style import s
from Controls.check_final_table import FinalTable
from Controls.datepicker import Datepicker
from Controls.dropdown import Dropdown
from utils.path import absolut_path
from utils.remove_element import remove_element
from Controls.tags_input import TagsInput
from tests.conftest import *



'''подготавливаем тестовые данные'''

url = 'https://demoqa.com/automation-practice-form'
phone = f'925{str(random.randint(1000000, 9999999))}'
mail = f'mailbox{str(random.randint(1, 10000))}@gmail.com'
list_names = ['Leonid', 'Victor', 'Roman', 'Alexandr', 'Sergey', 'Valentin']
list_lastnames = ['Borisov', 'Ivanov', 'Sergeev', 'Petrov', 'Romanov', 'Ozerov']
first_name = list_names[random.randint(0, len(list_lastnames)-1)]
last_name = list_lastnames[random.randint(0, len(list_lastnames)-1)]
mounth = str(9)
year = str(1987)
day = str(24)
picture = 'picture.jpg'
adress = 'USA, Texas, Green Street 15'


def test_form():

    """вынес в переменные малоинформативные селекторы"""
    gender_male = 'gender-radio-1'
    hobbie_music = 'hobbies-checkbox-3'
    hobbie_sports = 'hobbies-checkbox-1'
    hobbie_reading = 'hobbies-checkbox-2'
    # input_state = '[id="react-select-3-input"]'
    # input_city = '[id="react-select-4-input"]'
    # input_subject = '[id="subjectsInput"]'
    # select_year = '[class="react-datepicker__year-select"]'
    # select_mount = '[class ="react-datepicker__month-select"]'
    final_form = '[id="example-modal-sizes-title-lg"]'

    browser.open(url)
    remove_element('footer')

    browser.element('[class="main-header"]').should(have.text('Practice Form'))

    browser.element('[id="firstName"]').type(first_name)
    browser.element('[placeholder="Last Name"]').type(last_name)
    browser.element('[id="userEmail"]').type(mail)

    browser.element(f'[for="{gender_male}"]').click()

    browser.element('[placeholder = "Mobile Number"]').type(phone)

    date_of_birth = Datepicker(s('#dateOfBirthInput'))
    date_of_birth.choose_date(year=year, month=mounth, day=day)

    """OR 
    # browser.element('[id="dateOfBirthInput"]').click()
    # browser.element(select_year).click().element(f'[value="{year}"]').click()
    # browser.element(select_mount).click().element(f'[value="{mount}"]').click()
    # browser.element('[aria-label="Choose Saturday, October 24th, 1987"]').click()
    """


    subjects = TagsInput(browser.element('#subjectsInput'))
    subjects.add('English')
    # select_dropdown(input_subject, 'English')

    browser.element(f'[for="{hobbie_reading}"]').click()
    browser.element(f'[for="{hobbie_sports}"]').click()
    browser.element(f'[for="{hobbie_music}"]').click()

    browser.element('#uploadPicture').send_keys(absolut_path(picture))

    browser.element('[id="currentAddress"]').type(adress)

    Dropdown(browser.element('#state')).select(option='NCR')
    Dropdown(browser.element('#city')).autocomplete(option='Noida')
    # select_dropdown(input_state, 'NCR')
    # select_dropdown(input_city, 'Noida')

    remove_element('#fixedban')

    browser.element('[id="submit"]').click()

    """проверяем созданную форму"""

    final_table = FinalTable
    final_table(0, f'{first_name} {last_name}').result_assert()
    final_table(1, f'{mail}').result_assert()
    final_table(2, 'Male').result_assert()
    final_table(3, f'{phone}').result_assert()
    final_table(4, '24 October,1987').result_assert()
    final_table(5, 'English').result_assert()
    final_table(6, 'Reading, Sports, Music').result_assert()
    final_table(7, 'picture.jpg').result_assert()
    final_table(8, 'USA, Texas, Green Street 15').result_assert()
    final_table(9, 'NCR Noida').result_assert()

    """OR"
    browser.element(final_form).should(have.text('Thanks for submitting the form'))
    cells_of_row(1).should(have.text(f'{first_name} {last_name}'))
    cells_of_row(2).should(have.text(f'{mail}'))
    cells_of_row(3).should(have.text('Male'))
    cells_of_row(4).should(have.text(f'{phone}'))
    cells_of_row(5).should(have.text('24 October,1987'))
    cells_of_row(6).should(have.text('English'))
    cells_of_row(7).should(have.text('Reading, Sports, Music'))
    cells_of_row(8).should(have.text('picture.jpg'))
    cells_of_row(9).should(have.text('USA, Texas, Green Street 15'))
    cells_of_row(10).should(have.text('NCR Noida'))
    """


# """бонусное задание, закомментировал, чтобы пока не мешало. Требует актуализации"""

# def test_table():
#     """добавить запись"""
#     browser.open('https://demoqa.com/webtables')
#     browser.element('[id="addNewRecordButton"]').click()
#     browser.element('[id="firstName"]').type(first_name)
#     browser.element('[id="lastName"]').type(last_name)
#     browser.element('[id="userEmail"]').type(mail)
#     browser.element('[id="age"]').type('34')
#     browser.element('[id="salary"]').type('120000')
#     browser.element('[id ="department"]').type('it')
#     browser.element('[id="submit"]').click()
#
#     #проверяем запись
#
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][2]').should(have.text(f'{last_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][3]').should(have.text('34'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][4]').should(have.text(f'{mail}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][5]').should(have.text('120000'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][6]').should(have.text('it'))
#
#
#     """правим вторую строку"""
#
#
#     browser.element('[id="edit-record-2"]').click()
#     browser.element('[id="firstName"]').clear().type(first_name)
#     browser.element('[id="lastName"]').clear().type(last_name)
#     browser.element('[id="userEmail"]').clear().type(mail)
#     browser.element('[id="age"]').clear().type('34')
#     browser.element('[id="salary"]').clear().type('1200000')
#     browser.element('[id = "department"]').clear().type('it')
#     browser.element('[id="submit"]').click()
#
#     #проверяем правки
#
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][2]').should(have.text(f'{last_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][3]').should(have.text('34'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][4]').should(have.text(f'{mail}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][5]').should(have.text('120000'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][6]').should(have.text('it'))
#
#     #удаляем третью
#
#     browser.element('[id="delete-record-3"]').click()
#
#     #проверяем
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][3]//*[@class="rt-td"][1]').should(have.no.text('Kierra'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][3]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
#
#
#
#
# def test_table():
#     """добавить запись"""
#     browser.open('https://demoqa.com/webtables')
#     browser.element('[id="addNewRecordButton"]').click()
#     browser.element('[id="firstName"]').type(first_name)
#     browser.element('[id="lastName"]').type(last_name)
#     browser.element('[id="userEmail"]').type(mail)
#     browser.element('[id="age"]').type('34')
#     browser.element('[id="salary"]').type('120000')
#     browser.element('[id ="department"]').type('it')
#     browser.element('[id="submit"]').click()
#
#     #проверяем запись
#
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][2]').should(have.text(f'{last_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][3]').should(have.text('34'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][4]').should(have.text(f'{mail}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][5]').should(have.text('120000'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][6]').should(have.text('it'))
#
#
#     """правим вторую строку"""
#
#
#     browser.element('[id="edit-record-2"]').click()
#     browser.element('[id="firstName"]').clear().type(first_name)
#     browser.element('[id="lastName"]').clear().type(last_name)
#     browser.element('[id="userEmail"]').clear().type(mail)
#     browser.element('[id="age"]').clear().type('34')
#     browser.element('[id="salary"]').clear().type('1200000')
#     browser.element('[id = "department"]').clear().type('it')
#     browser.element('[id="submit"]').click()
#
#     #проверяем правки
#
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][2]').should(have.text(f'{last_name}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][3]').should(have.text('34'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][4]').should(have.text(f'{mail}'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][5]').should(have.text('120000'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][6]').should(have.text('it'))
#
#     #удаляем третью
#
#     browser.element('[id="delete-record-3"]').click()
#
#     #проверяем
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][3]//*[@class="rt-td"][1]').should(have.no.text('Kierra'))
#     browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][3]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
#


















