from django.shortcuts import render
from .models import Produs, Order
from django.core.paginator import Paginator


def index(request):
    product_object = Produs.objects.all()

    # Cautare produs
    product_name = request.GET.get('product_name')
    if(product_name != '' and product_name is not None):
        product_object = product_object.filter(name__icontains=product_name)

    # Paginare
    paginator = Paginator(product_object, 3)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object': product_object})


def details(request, id):
    # Pagina de produs
    product = Produs.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product})


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items', '')
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")

        order = Order(items=items, name=name, email=email,
                      address=address, city=city, state=state, zipcode=zipcode)
        order.save()

    return render(request, 'shop/checkout.html',)
