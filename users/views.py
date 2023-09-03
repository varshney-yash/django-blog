from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import userRegisterForm

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Thanks for joining, {username}. Please login to continue!')
            return redirect('user-login')
    else:
        form = userRegisterForm()
    context = {'form':form}
    return render(request,'users/register.html',context)
     
def user_login(request):
    return render(request,'users/login.html')