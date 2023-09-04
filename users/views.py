from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import userRegisterForm,UserUpdateForm,ProfileUpdateForm

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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    if u_form.is_valid():
        u_form.save()
    if p_form.is_valid():
        p_form.save()

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/profile.html',context)

# test image upload
from .models import Profile
def upload_image(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to create a new Profile instance with the uploaded image
            form.save()
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'users/upload_image.html', {'form': form})