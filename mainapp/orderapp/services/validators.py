from django import forms


def validate_city(value: str) -> None:
    """ Валидирует поле город в форме заказа"""
    if len(value) < 3:
        raise forms.ValidationError('Слишком короткое название ')

    if value.isascii():
        raise forms.ValidationError('Только кириллица')

    if value.isnumeric():
        raise forms.ValidationError('Только буквы')

    if value.isspace():
        raise forms.ValidationError('Название не может содержать только пробелы')


def validate_address(value: str) -> None:
    """ Валидирует поле адрес в форме заказа"""

    if len(value) < 5:
        raise forms.ValidationError('Слишком короткое название')

    if value.isascii():
        raise forms.ValidationError('Только кириллица')

    if value.isnumeric():
        raise forms.ValidationError('Только буквы')

    if value.isspace():
        raise forms.ValidationError('Название не может содержать только пробелы')


def validate_postal_code(value: str) -> None:
    """ Валидирует поле индекс в форме заказа"""

    print(len(value))
    if len(value) != 6:
        raise forms.ValidationError('Индекс должен состоять из 6 цифр')

    if value.isalpha():
        raise forms.ValidationError('Только цифры')

    if value.isspace():
        raise forms.ValidationError('Индекс не может состоять только из пробелов')
