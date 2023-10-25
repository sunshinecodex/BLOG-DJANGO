from django.views.generic.base import View
from django.shortcuts import render  #renderizar vista
from django.views.generic.base import View


class HelloWorld(View):
    def get(self,request):
        data={
            'name': 'Agustin Navarro Galdon V2',
            'years': 28,
            'codes':['python', 'Django', 'React']
        }
        return render(request,'hello_world.html', context=data)