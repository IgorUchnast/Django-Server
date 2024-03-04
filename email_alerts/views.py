from django.shortcuts import render

from configurations import settings
from .models import Customer
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template 
from django.shortcuts import render, redirect
# from .forms import CustomForm

def send_email_notification(device_name, temp_value):
    customers = Customer.objects.filter(status='active')  # Assuming you want to notify only active customers

    for customer in customers:
        email_address = customer.email_address

        message = f'Warning: Check your Shieldbox! Temperature is {temp_value}°C.'

        subject = 'Temperature Alert'
        context = {'name': customer.name, 'message': message}
        message = get_template('emailapp/email.html').render(context)
        email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [email_address])
        email.content_subtype = "html"
        email.send()

# def index(request):
#     return render(request,'emailapp/index.html')
    
# def sendto_allcustomers(request):
#     customers = Customer.objects.all()
#     for customers in customers:
#         print(customers.name)
#         email_address = customers.email_address
    
#         message = 'Warning: Check your Shieldbox!'
    
#         subject = 'New Products'
#         context = {'name': customers.name,'message': message}
#         message = get_template('emailapp/email.html').render(context)
#         email = EmailMessage(subject, message,"Warning", [email_address])
#         email.content_subtype = "html" 
#         email.send()
    
#     return redirect('index')
# def send_email_notification(device_name, temp_value):
#     customers = Customer.objects.filter(status='active')  # Assuming you want to notify only active customers

#     for customer in customers:
#         email_address = customer.email_address

#         message = f'Warning: Check your Shieldbox! Temperature is {temp_value}°C.'

#         subject = 'Temperature Alert'
#         context = {'name': customer.name, 'message': message}
#         message = get_template('emailapp/email.html').render(context)
#         email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [email_address])
#         email.content_subtype = "html"
#         email.send()