from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login/')
def home_view(request):
    return render(request, "index.html")

def signup_view(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    
    
    context ={"form":form}
    return render(request, 'signup.html',context)

def login(request):
    context = {}
    return render(request, 'login.html',context)    