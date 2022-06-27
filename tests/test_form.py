
from conftest import *

'''подготавливаем тестовые данные, Добавил random чтобы данные не повторялись'''

url = 'https://demoqa.com/automation-practice-form'
phone = f'925{str(random.randint(1000000, 9999999))}'
mail = f'mailbox{str(random.randint(1, 10000))}@gmail.com'
list_names = ['Leonid', 'Victor', 'Roman', 'Alexandr', 'Sergey', 'Valentin']
list_lastnames = ['Borisov', 'Ivanov', 'Sergeev', 'Petrov', 'Romanov', 'Ozerov']
first_name = list_names[random.randint(0, len(list_lastnames)-1)]
last_name = list_lastnames[random.randint(0, len(list_lastnames)-1)]
mount = str(random.randint(0,11))
year = str(random.randint(1900, 2022))
day = str(random.randint(1, 30))
picture = r'C:\Users\roman\PycharmProjects\demoqa\picture.jpg'
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
    browser.element('[class="react-datepicker__week"]').click()
    browser.element('[id="subjectsContainer"]')
    browser.element('[id="subjectsInput"]').type("English").press_tab()
    browser.element('[id="subjectsInput"]').type("Hindi").press_tab()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').type(picture)
    browser.element('[id="currentAddress"]').type(adress)
    browser.element('[id="react-select-3-input"]').type('NCR').press_tab()
    browser.element('[id="react-select-4-input"]').type('Noida').press_tab()
    del_element('#fixedban')
    browser.element('[id="submit"]').click()



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

    """правим вторую строку"""
    browser.element('[id="edit-record-2"]').click()
    browser.element('[id="firstName"]').clear().type(first_name)
    browser.element('[id="lastName"]').clear().type(last_name)
    browser.element('[id="userEmail"]').clear().type(mail)
    browser.element('[id="salary"]').clear().type('1250000')
    browser.element('[id = "department"]').clear().type('it')
    browser.element('[id="submit"]').click()

    """удаляем третью"""
    browser.element('[id="delete-record-3"]').click()
















