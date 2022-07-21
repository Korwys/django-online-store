from .models import Genders, ProductCategory


def genders_list(request):
    return {'gender_choise_list': Genders.objects.all()}

def product_categories(request):
    return {'categories': ProductCategory.objects.all()}
