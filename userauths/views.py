from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.

def register_view(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.changed_data.get("username")
            
    else:
        form = UserRegisterForm()
    
    context = {
        'form':form,
    }
    return render(request, "userauths/sign-up.html", context)