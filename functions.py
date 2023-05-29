def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_find = input('Введите данные для поиска: ')
    print(f'\n {search(data, data_to_find)} \n')


def search(book: list[str], info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    find = [i for i in book if info in i]
    if len(find) == 0:
        return 'Ничего не найдено'
    elif len(find) == 1:
        return find[0]
    elif len(find) > 1:
        print()
        print('Нашлось несколько результатов')
        info_1 = input('Уточните поиск: ')
        return search(book, info_1)