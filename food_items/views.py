from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm
    
def list_food_items(request):
    items = FoodItem.objects.all()
    return render(request, 'food_items/list.html', {'items': items})

def add_food_item(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_food_items')
    else:
        form = FoodItemForm()
    return render(request, 'food_items/form.html', {'form': form})

def edit_food_item(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    if request.method == "POST":
        form = FoodItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_food_items')
    else:
        form = FoodItemForm(instance=item)
    return render(request, 'food_items/form.html', {'form': form})

def delete_food_item(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('list_food_items')
    return render(request, 'food_items/confirm_delete.html', {'item': item})
