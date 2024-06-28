from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import TODO

# Create your views here.
def index(request):
    # return HttpResponse("hello world")
    todos = TODO.objects.order_by('-id')
    return render(request,'todo/index.html',{'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        TODO.objects.create(title = title, description = description)
    # return render(request,'todo/index.html')
    return redirect('index_page')

def marking(request, id):
    
    todo = TODO.objects.get(id = id)
    todo.is_done = True
    todo.save()
    return redirect('index_page')

def delete(request, id):
    TODO.objects.get(id = id).delete()
    return redirect('index_page')
    
    
        
