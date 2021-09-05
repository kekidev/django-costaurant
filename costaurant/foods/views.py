from django.shortcuts import render
from datetime import datetime
from foods.models import Menu

def index(req):
  context = {
    "date": datetime.today().date(),
    "menus": Menu.objects.all()
  }
  return render(req, 'foods/index.html', context=context)

def food_detail(req, pk):
  try:
    context = {
      "menu": Menu.objects.get(id=pk)
    }
    
    return render(req, 'foods/details.html', context=context)
  except:
    return render(req, "foods/404.html")