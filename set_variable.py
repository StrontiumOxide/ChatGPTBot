import os


def set_envirion(filename: str) -> None:
    """Функция по установке переменных в виртуальное окружение"""

    with open(file=filename, mode='r', encoding='utf-8') as file:
        reader = file.readlines()

    print('\nЗагрузка...')
    for order, row in enumerate(reader):
        try:
            key, value = row.strip().split(sep=' = ', maxsplit=1)
        except ValueError:
            key, value = 'Unknown', 'Unknown'
            status = 'Ошибка'
            args = row.strip()
        else:
            os.environ[key] = value
            status = 'Успешно'
            args = 'Empty'
        finally:
            print(f'{order+1}) Статус: "{status}", Ключ: "{key}", Значение: "{value}", Args: "{args}"')

    print('\nПеременные виртуального окружения')
    for order, k in enumerate(os.environ.items()):
        print(f"{order+1}) {k[0]} = {k[1]}")
    input('\nНажмите любую кнопку для завершения...')


def main() -> None:
    """Главная функция"""

    print('\nЗагрузчик переменных в виртуальное окружение')
    filename = input('Введите имя файла: ')
    set_envirion(filename=filename)


if __name__ == "__main__":
    main()
