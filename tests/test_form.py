
from application_manager import form, final_table
from tests.conftest import *
from data.data import *

def test_form():

    browser.open(url)
    remove_element('footer')

    form.set_first_name(first_name)
    form.set_last_name(last_name)
    form.set_mail(mail)
    form.choose_gender(gender_male)
    form.set_phone(phone)
    form.set_date_of_birth(year, month, day)
    form.set_subjects(subject_english)
    form.set_hobbie(hobbie_music)
    form.upload_picture(picture)
    form.set_address(adress)
    form.set_state('NCR')
    form.set_city('Noida')

    remove_element('#fixedban')

    form.submit()


    """проверяем созданную форму"""

    final_table(0, f'{first_name} {last_name}').result_assert()
    final_table(1, f'{mail}').result_assert()
    final_table(2, 'Male').result_assert()
    final_table(3, f'{phone}').result_assert()
    final_table(4, '24 October,1987').result_assert()
    final_table(5, 'English').result_assert()
    final_table(6, 'Music').result_assert()
    final_table(7, 'picture.jpg').result_assert()
    final_table(8, 'USA, Texas, Green Street 15').result_assert()
    final_table(9, 'NCR Noida').result_assert()










