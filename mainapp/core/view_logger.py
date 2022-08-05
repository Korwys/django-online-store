import functools
import logging

from django.shortcuts import render
from django.db import transaction

logger = logging.getLogger('view_logger')


def view_logger(func):
    """
    Общий декоратор для вьюшек,отлавливает эксепшины, которые не были перехвачены внутри вьюхи.
    Логирует в отдельный файл logs/view.log
    Возвращает юзеру страницу с описанием проблемы.
    """
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return func(request, *args, **kwargs)
        except Exception as e:
            logger.critical(e.chain)
            return render(request, 'mainapp/error.html', )

    return wrapper
