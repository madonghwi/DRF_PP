from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, SigninForm, ModifyForm


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            return redirect('signin')
    else:
        form = SignupForm()
    return render(request, 'user/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)  # 이메일 대신 username 인자로 변경
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, '이메일 또는 비밀번호가 일치하지 않습니다.')
    else:
        form = SigninForm()
    return render(request, 'user/signin.html', {'form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('index')


@login_required
def modify(request):
    if request.method == 'POST':
        form = ModifyForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('index')
    else:
        form = ModifyForm(instance=request.user)
    return render(request, 'user/modify.html', {'form': form})


@login_required
def withdrawal(request):
    if request.method == 'POST' or request.method == 'GET':
        request.user.delete()
        logout(request)
        return redirect('index')
