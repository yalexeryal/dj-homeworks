from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'home': reverse('home')
        'omlet': reverse('omlet')
        'pasta': reverse('pasta')
        'buter': reverse('bater')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def recipes(request):
    servings = int(request.Get.get('servings', 1))
    recipe = {}
    for keys in DATA.keys():
        if keys in request.path:
            recipe = DATA.get(keys).copy()
    template_name = 'calculator/index/index.html'
    for key in recipe.keys():
        recipe[key] = recipe.get(key) * servings
    context = {
        'recipe': recipe,
    }
    return render(request, template_name, context)
