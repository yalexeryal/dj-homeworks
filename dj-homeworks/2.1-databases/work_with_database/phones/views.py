from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_query = Phone.objects.all()
    filter_phone_name=request.GET.get('sort')
    print(filter_phone_name)
    if filter_phone_name == 'name':
        phones_query = phones_query.order_by('name')
    if filter_phone_name == 'min_price':
        phones_query = phones_query.order_by('price')
    if filter_phone_name == 'max_price':
        phones_query = phones_query.order_by('-price')
    context = {'phones': phones_query}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_query = Phone.objects.get(slug=slug)
    context = {'phone': phone_query}
    return render(request, template, context)