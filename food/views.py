from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import FoodItem



class IndexClassListView(generic.ListView):
    """
    Generic class-based view for displaying a list of items.
    """
    model = FoodItem
    template_name = 'food/index.html'
    context_object_name = 'item_list'


class FoodItemDetailView(generic.DetailView):
    """
    Class-based detailed view for a food item.
    """
    model = FoodItem
    template_name = 'food/detail.html'
    # context_object_name = 'item'


class FoodItemCreateView(generic.CreateView):
    """
    Class-based view for creating a food item.
    The dispatch method is used to ensure that only logged in users can create a food item.
    """
    model = FoodItem
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item_form.html'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


class FoodItemUpdateView(generic.UpdateView):
    """
    Class-based view for updating a food item.
    """
    model = FoodItem
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item_form.html'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


class FoodItemDeleteView(generic.DeleteView):
    """
    Class-based view for deleting a food item.
    """
    model = FoodItem
    success_url = '/food/'
    template_name = 'food/item_delete.html'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Views that are no longer used, but are kept for reference. Function based views

# def delete_item(request, id):
#     item = FoodItem.objects.get(pk=id)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('food:index')
#     return render(request, 'food/item_delete.html', {'item': item})

# def update_item(request, id):
#     item = FoodItem.objects.get(pk=id)
#     form = FoodItemForm(request.POST or None, instance=item)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item_form.html', {'form': form, 'item': item})

# def detail(request, item_id):
#     item = FoodItem.objects.get(pk=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)