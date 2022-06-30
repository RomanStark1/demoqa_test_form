import os
import webbrowser

from selene import command

from conftest import *

'''подготавливаем тестовые данные, Добавил random чтобы данные не повторялись'''

url = 'https://demoqa.com/automation-practice-form'
phone = f'925{str(random.randint(1000000, 9999999))}'
mail = f'mailbox{str(random.randint(1, 10000))}@gmail.com'
list_names = ['Leonid', 'Victor', 'Roman', 'Alexandr', 'Sergey', 'Valentin']
list_lastnames = ['Borisov', 'Ivanov', 'Sergeev', 'Petrov', 'Romanov', 'Ozerov']
first_name = list_names[random.randint(0, len(list_lastnames)-1)]
last_name = list_lastnames[random.randint(0, len(list_lastnames)-1)]
mount = str(9)
year = str(1987)
day = str(24)
picture = 'picture.jpg'
adress = 'USA, Texas, Green Street 15'
state = 'NCR'
city = 'Delhi'


'''функция при помощи которой можно скрыть элементы мешающие тесту'''
def del_element(elem):
    # return browser.execute_script("$('footer').remove();")
    scr = f"$('{elem}').remove();"
    return browser.execute_script(scr)

'''тестируем форму'''
def test_form():

    browser.open(url)
    del_element('footer')

    browser.element('[class="main-header"]').should(have.text('Practice Form'))

    browser.element('[id="firstName"]').type(first_name)
    browser.element('[placeholder="Last Name"]').type(last_name)
    browser.element('[id="userEmail"]').type(mail)

    browser.element('[for="gender-radio-1"]').click()

    browser.element('[placeholder = "Mobile Number"]').type(phone)

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element(f'[value="{year}"]').click()
    browser.element('[class ="react-datepicker__month-select"]').click().element(f'[value="{mount}"]').click()
    browser.element('[aria-label="Choose Saturday, October 24th, 1987"]').click()


    browser.element('[id="subjectsInput"]').type("English").press_tab()
    browser.element('[id="subjectsInput"]').type("Hindi").press_tab()

    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath(f'../{picture}'))

    browser.element('[id="currentAddress"]').type(adress)
    browser.element('[id="react-select-3-input"]').type('NCR').press_tab()
    browser.element('[id="react-select-4-input"]').type('Noida').press_tab()

    del_element('#fixedban')

    browser.element('[id="submit"]').click()

    """проверяем созданную форму"""

    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.element(f'//*[@class="table-responsive"]//tr[1]//td[2]').should(have.text(f'{first_name} {last_name}'))
    browser.element(f'//*[@class="table-responsive"]//tr[2]//td[2]').should(have.text(f'{mail}'))
    browser.element(f'//*[@class="table-responsive"]//tr[3]//td[2]').should(have.text('Male'))
    browser.element(f'//*[@class="table-responsive"]//tr[4]//td[2]').should(have.text(f'{phone}'))
    browser.element(f'//*[@class="table-responsive"]//tr[5]//td[2]').should(have.text('24 October,1987'))
    browser.element(f'//*[@class="table-responsive"]//tr[6]//td[2]').should(have.text('English, Hindi'))
    browser.element(f'//*[@class="table-responsive"]//tr[7]//td[2]').should(have.text('Reading, Sports, Music'))
    browser.element(f'//*[@class="table-responsive"]//tr[8]//td[2]').should(have.text('picture.jpg'))
    browser.element(f'//*[@class="table-responsive"]//tr[9]//td[2]').should(have.text('USA, Texas, Green Street 15'))
    browser.element(f'//*[@class="table-responsive"]//tr[10]//td[2]').should(have.text('NCR Noida'))


def test_table():
    """добавить запись"""
    browser.open('https://demoqa.com/webtables')
    browser.element('[id="addNewRecordButton"]').click()
    browser.element('[id="firstName"]').type(first_name)
    browser.element('[id="lastName"]').type(last_name)
    browser.element('[id="userEmail"]').type(mail)
    browser.element('[id="age"]').type('34')
    browser.element('[id="salary"]').type('120000')
    browser.element('[id ="department"]').type('it')
    browser.element('[id="submit"]').click()

    #проверяем запись

    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][2]').should(have.text(f'{last_name}'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][3]').should(have.text('34'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][4]').should(have.text(f'{mail}'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][5]').should(have.text('120000'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][4]//*[@class="rt-td"][6]').should(have.text('it'))


    """правим вторую строку"""


    browser.element('[id="edit-record-2"]').click()
    browser.element('[id="firstName"]').clear().type(first_name)
    browser.element('[id="lastName"]').clear().type(last_name)
    browser.element('[id="userEmail"]').clear().type(mail)
    browser.element('[id="age"]').clear().type('34')
    browser.element('[id="salary"]').clear().type('1200000')
    browser.element('[id = "department"]').clear().type('it')
    browser.element('[id="submit"]').click()

    #проверяем правки

    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][2]').should(have.text(f'{last_name}'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][3]').should(have.text('34'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][4]').should(have.text(f'{mail}'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][5]').should(have.text('120000'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][2]//*[@class="rt-td"][6]').should(have.text('it'))

    #удаляем третью

    browser.element('[id="delete-record-3"]').click()

    #проверяем
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][3]//*[@class="rt-td"][1]').should(have.no.text('Kierra'))
    browser.element('//*[@class="rt-table"]//*[@class="rt-tbody"]//*[@class="rt-tr-group"][3]//*[@class="rt-td"][1]').should(have.text(f'{first_name}'))
















