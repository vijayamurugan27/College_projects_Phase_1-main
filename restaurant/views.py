from django.shortcuts import render, redirect, get_object_or_404

from restaurant.models import Foods

from .forms import ProductForm, OrderForm

# Create your views here.
def home(request):
    food = Foods.objects.all()
    context = {'food':food}
    return render(request, 'restaurant/home.html', context)

def order(request, id):
    obj = get_object_or_404(Foods, id =id)
    form = OrderForm(request.POST or None, instance = obj)
    data = Foods.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('restaurant:home')
    context = {'form':form, 'data':data}
    return render(request, 'restaurant/order.html', context)

def kart(request):
    Ordered_items = Foods.objects.filter(order_status = True)
    # print("Ordered Items :", Ordered_items)
    price = Foods.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        # print(price.price)
        # print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        # print(total)

    # print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'restaurant/kart.html', context)