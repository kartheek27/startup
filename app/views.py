from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Customer
import random
import string

# Create your views here.
def Home(request):
    return render(request,'index.html')

def customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        state = request.POST.get('state')
        district = request.POST.get('district')
        mandal = request.POST.get('mandal')
        village = request.POST.get('village')
        pin = request.POST.get('pin')

        # Basic form validation (you can add more if needed)
        if len(phone) == 10 and len(pin) == 6:
            # Save the data to the database
            digits = ''.join(random.choices(string.digits, k=2))
            letters = ''.join(random.choices(string.ascii_uppercase, k=4))
            user= letters + digits
            Customer.objects.create(
                userid=user,
                name=name,
                phone=phone,
                state=state,
                district=district,
                mandal=mandal,
                village=village,
                pin=pin
            )
            
            return HttpResponseRedirect(f'/form-success/{user}')  # Redirect after successful submission
        else:
            error_message = "Please ensure the phone number is 10 digits and the pin code is 6 digits."
            return render(request, 'customer_form.html', {'error_message': error_message})

    return render(request, 'customer.html')

def form_success_view(request,id):
    customer = get_object_or_404(Customer, userid=id)

    if request.method == 'POST':
        mpin_new = request.POST.get('mpin')  # Assuming you're getting the new MPIN from a form

        # Update the mpin field
        customer.mpin = mpin_new
        customer.save(update_fields=['mpin'])  # Save only the 'mpin' field

        # After updating, you can redirect or render a response
        return redirect('login_page')
    
    return render(request,'form_success.html',{'user_id': id})

def login_page(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        mpin = request.POST.get('mpin')

        if Customer.objects.filter(userid=userid, mpin=mpin).exists():
            messages.success(request, 'Login successful')
            return render(request, 'user_home.html', {'userid': userid})

    # If the request is GET, just render the login page
    return render(request, 'login.html')

