import random

url = 'https://demoqa.com/automation-practice-form'
phone = f'925{str(random.randint(1000000, 9999999))}'
mail = f'mailbox{str(random.randint(1, 10000))}@gmail.com'
list_names = ['Leonid', 'Victor', 'Roman', 'Alexandr', 'Sergey', 'Valentin']
list_lastnames = ['Borisov', 'Ivanov', 'Sergeev', 'Petrov', 'Romanov', 'Ozerov']
first_name = list_names[random.randint(0, len(list_lastnames)-1)]
last_name = list_lastnames[random.randint(0, len(list_lastnames)-1)]
month = str(9)
year = str(1987)
day = str(24)
subject_english = 'English'
picture = 'picture.jpg'
adress = 'USA, Texas, Green Street 15'
date = '24 Oct,1987'

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

