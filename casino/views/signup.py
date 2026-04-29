from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from casino.models import Users

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'registration/signup.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup.html', {
                'error': 'Username already exists'
            })
        
        user = User.objects.create_user(
            username=username,
            password=password
        )

        Users.objects.create(user=user)

        return redirect('login')
    
    return render(request, 'registration/signup.html')