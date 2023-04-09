from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FoodItemForm
from .models import FoodItem
from django.template import loader


# Create your views here.
def index(request):
    item_list = FoodItem.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)

def items(request):
    return HttpResponse("You're at the food items.")

def detail(request, item_id):
    item = FoodItem.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', {'form': form})

def update_item(request, id):
    item = FoodItem.objects.get(pk=id)
    form = FoodItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item_form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = FoodItem.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item_delete.html', {'item': item})
