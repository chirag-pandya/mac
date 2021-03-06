from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product, Contact, Orders
from math import ceil


# create your views here
def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products, range(1,nSlides),nSlides],
    #             [products, range(1,nSlides),nSlides]]
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")
def search(request):
    return render(request, "shop/search.html")

def productView(request, myid):
    # Fetch the product using id.

    product = Product.objects.filter(id=myid)
    return render(request, "shop/productView.html", {'product':product[0]})

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        print(name, email, address, city, state, zip_code, phone)

        # order = Orders(name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone )
        order = Orders(name=name)
        order.save()
    return render(request, "shop/checkout.html")
