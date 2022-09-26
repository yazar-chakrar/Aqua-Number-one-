from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import CreateFoodForm

def create_food(request):
    if request.method == 'POST':
        form = CreateFoodForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.save()
            return HttpResponseRedirect('/thanks/')
    else :
        form = CreateFoodForm()
            
    return render(request, 'create_food.html', {'form': form})