from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(requests):
    # return HttpResponse('Hello World!') # alt + enter 로 간단히 import
    if requests.method == 'POST':

        temp = requests.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(requests, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(requests, 'accountapp/hello_world.html', context={'text': 'GET METHOD!'})