from django import template

register = template.Library()


@register.simple_tag
def make_custom_url_for_djnago_filter(value: str, field_name: str, urlencode=None) -> str:
    """Функция соединяет GET параметры от Django-filter и GET параметр от пагинатора.
    Возвращает строку вида -> ?page=3&brand=3..."""

    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda x: x.split('=')[0] != field_name, querystring)
        encode_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encode_querystring}'

    return url


@register.simple_tag
def sorting_filter(value: str, field_name: str, urlencode=None) -> str:
    """Функция соединяет GET параметры от Django-filter и GET параметр сортировки.
        Возвращает строку вида -> ?sorting=price&brand=3..."""

    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda x: x.split('=')[0] != field_name, querystring)
        encode_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encode_querystring}'

    return url
