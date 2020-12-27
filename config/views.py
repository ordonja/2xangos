from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        return render(request, 'index.html', {'user':user})
    return render(request, 'index.html')


def twredirect(request):
    return redirect()

def index(request):
    return render(request, 'index.html')

def registro(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            xango = form.save()
            login(request,xango)
            return render(request, 'index.html')
    context['form']=form
    return render(request, 'directorio/registro.html', context)
