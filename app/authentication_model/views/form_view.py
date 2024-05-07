from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email is None or email == '':
            messages.error(request, 'Authentication failed')
            return redirect('login')

        if password is None or password == '':
            messages.error(request, 'Authentication failed')
            return redirect('login')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                user = auth.authenticate(username=user.username, password=password)
                if user is not None:
                    auth.login(request, user)
                    messages.success(request, 'Logged in')
                    return redirect('dashboard')
                else:
                    messages.error(request,'Authentication failed')
                    return redirect('login')
            else:
                messages.error(request,'Invalid password')

        except User.DoesNotExist:
            messages.error(request, 'User not registered')
            return redirect('login')

        except User.MultipleObjectsReturned:
            messages.error(request, 'Multiple users found with this email. Please contact support.')
            return redirect('login')

    return render(
        request=request,
        template_name='authentication_model/pages/login.html'
)

def logout(request):
    ...

def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print('Sign in: ', name, email, password, password2)

        if name.strip() is None or name.strip() == '':
            messages.error(request,"Field name is empty")
            return redirect('signin')

        if '.com' not in email:
            messages.error(request,"Field email is empty")
            return redirect('signin')

        if password2!=password:
            messages.error(request,"Passwords do not match")
            return redirect('signin')

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email is already registered!')
            return redirect('signin')
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        messages.success(request,"User register successfully!")
        return redirect('login')

    return render(
        request=request,
        template_name='authentication_model/pages/signin.html'
    )

@login_required
def dashboard(request):
    user = request.user

    return render(
        request=request,
        template_name='authentication_model/pages/dashboard.html',

    )
