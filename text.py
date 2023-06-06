main_menu = '''\nГлавное меню:
1. Открыть файл
2. Записать файл
3. Показать контакт
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход\n'''


input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта'

save_successful = 'Телефонная книга успешно сохранена'


pb_empty = 'Телефонная книга пуста или не окрыта'

input_new_contact = 'Ведите данные нового контакта: '

new_contact = {'name': 'Введите имя: ',
               'phone': 'Введите телефон: ',
               'comment': 'Введите коментарий: '}


def new_contact_successful(name: str):
    return f'Контакт {name} успешно добавлен'


input_search = 'Что будем искать: '


def empty_search(word) -> str:
    return f'Контакты содержащие слово "{word}" не найдены'


input_change = 'Какой контакт будем менять: '
input_index = 'Введите индекс контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, чобы не менять: '


def change_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен'


index_del_contact = 'Введите индекс удаляемого контакта: '


def del_contact(name: str):
    return f'Контакт {name} успешно удален'
