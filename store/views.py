from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from products.models import Products, ProductImages, ProductOption, ProductVariation
from marchants.forms import CustomUserCreationForm
from django.http import JsonResponse
from store.forms import LoginForm
from paystackapi.transaction import Transaction
from django.db.models import OuterRef, Subquery

# Create your views here.

def index(request):
    product = Products.objects.all()[:10]
    return render(request, 'index.html', {'product_list':product} )


    

def Signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, pasword=password)
            login(request, user)
            return redirect('home')
    else:
      form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})



def payement(request):
    if request.method == 'POST':
      refrence = request.POST.get('refrence')
      email = request.POST.get('email')
      amount = int(float(request.POST.get('amount')))
      response = Transaction.initialize(reference=refrence, amount=amount, email=email)
      return JsonResponse(response, status=200, safe=False)
    return JsonResponse({'error': 'could not add item to cart' }, status=400)
    

