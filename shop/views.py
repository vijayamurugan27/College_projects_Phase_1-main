from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Products, Customer

# Create your views here.
def home(request):
    return render(request, 'shop/home.html') 

def Shirts(request):
    shirts = Products.objects.all()
    context = {'shirts': shirts, }
    return render(request, 'shop/shirts.html', context)



from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class ShirtDetail(CreateView):
    model = Products
    fields = "__all__"
    template_name = 'shop/cbv/form.html'
    success_url = 'home'

# class ShirtList(ListView):
#     model = Products
#     template_name = 'library/cbv/stulist.html'


from shop.forms import ShopProductForm, ShopOrderForm

def order(request, id):
    obj = get_object_or_404(Products, id =id)
    form = ShopOrderForm(request.POST or None, instance = obj)
    data = Products.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('shop:Shirts')
    context = {'form':form, 'data':data}
    return render(request, 'shop/order.html', context)

def kart(request):
    Ordered_items = Products.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Products.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'shop/kart.html', context)

