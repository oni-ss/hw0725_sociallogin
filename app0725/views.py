from django.shortcuts import render, redirect, get_object_or_404
from .models import Pictures

def home(request):
    blog = Pictures.objects.all()
    return render(request, 'home.html', {'blog':blog})

def read(request, pk):
    blogs = get_object_or_404(Pictures, pk=pk)
    return render(request, 'detail.html', {'blogs':blogs})

def create(request):
    if request.method == 'POST':
        blog = Pictures()
        blog.image = request.FILES['p']
        blog.title = request.POST['t']
        blog.text = request.POST['b']
        blog.save()
        return redirect('home')
    else:
        return render(request, 'new.html')

def delete(request, pk):
    blog = get_object_or_404(Pictures, pk=pk)
    blog.delete()
    return redirect('home')

def update(request, pk):
    blog = get_object_or_404(Pictures, pk=pk)
    if request.method == 'POST':
        blog.title = request.POST['t']
        blog.image = request.FILES['p']
        blog.text = request.POST['b']
        blog.save()
        return redirect('home')
    return render(request, 'update.html', {'blog':blog})
    