from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from .forms import FoodItemForm
from .models import FoodItem



class IndexClassListView(generic.ListView):
    model = FoodItem
    template_name = 'food/index.html'
    context_object_name = 'item_list'

class FoodItemDetailView(generic.DetailView):
    model = FoodItem
    template_name = 'food/detail.html'
    # context_object_name = 'item'

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
