from .models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Contact
from .models import Payment,Order
from .forms import ReviewForm
# Create your views here.

imag=''
forms=''

def login_attempt(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request,"Succesful Logged-In")
            return redirect("/")

        else:
            # No backend authenticated the credentials
            messages.error(request,"Invalid Credentials ,Please Try Again")
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')




def register_attempt(request):
    print('loko')
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('mkokm')
        

        try:
            if User.objects.filter(username = username).first():
                messages.error(request, 'Username is taken.')
                return redirect('/register')
                print('mkokm6')


            if User.objects.filter(email = email).first():
                messages.error(request, 'Email is taken.')
                return redirect('/register')
                print('mkokm8')

            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            print('mkokm9')
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            print('mkokm11')
            messages.error(request, ' You have been registered')
            messages.error(request, ' if you are not redirected to a thank you page then plz manually login as it may be due to server issue of smtp  ,regards Arya Sah')
            send_mail_after_registration(email,auth_token)
            print('mkokm10')
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'accounts/register.html')

def success(request):
    return render(request , 'accounts/success.html')


def token_send(request):
    return render(request , 'accounts/token_send.html')

def ordersuccess(request):
    return render(request , 'accounts/ordersuccess.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/success')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'accounts/error.html')


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    global imag
    global forms
    imag=Review.objects.all()
    forms = ReviewForm()
    if request.method == "POST":
        uname = request.POST.get('name')
        
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        
        messages.success(request, 'Your message has been sent!')
#         subject = 'Contact'
#         message = f'Username {uname} Email :{email} Subject: {subject} Message:{message}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = ['aryasah30@gmail.com']
#         send_mail(subject, message , email_from ,recipient_list )
    return render(request, 'accounts/home.html', {'imag':imag, 'forms':forms,})
                  
def review(request):
       global forms
       if request.method == "POST":
        forms = ReviewForm(request.POST, request.FILES)
       if forms.is_valid():
        forms.save()
       forms = ReviewForm()
       global imag
       imag=Review.objects.all()
       messages.success(request, 'Thank You For Your Reviews It is submitted succesfully')

                  
     return redirect('/')
               





def about(request):
    return render(request, 'accounts/about.html') 

def contact(request):
    print('jh')
    if request.method == "POST":
        print('nvbcg')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        city = request.POST.get('city')
        datetim = request.POST.get('date')
        file= request.POST.get('filename')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        medname=request.POST.get('subject')
        contacted = Order(fname=fname,lname=lname, email=email,city=city,file=file, phone=phone, desc=desc, date =datetim,medname=medname,)
        contacted.save()
        messages.success(request, 'Your message has been sent!')
        return redirect('/payment')
        subject = 'Order Deatails'
        message = f'{fname} {lname} {email} {phone}{medname} {desc} {city} {datetim} {file}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message , email_from ,recipient_list ) 
        print(message)
    return render(request, 'accounts/contact.html')

def logoutUser(request):
    logout(request)
    messages.success(request,"Succesful Logout")

    return redirect("/accounts/login")




def send_mail_after_registration(email , token):
    
    subject = ' Thank you for registering with us Your accounts need to be verified '
    message = f'Hi  paste the link to verify your account http://aryasahmedicine.herokuapp.com/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
   
    send_mail(subject, message , email_from ,recipient_list )
    
    return redirect('/token')



def payment(request):
    print('jh')
    if request.method == "POST":
        uname = request.POST.get('username')
        
        year = request.POST.get('year')
        month = request.POST.get('month')
        cardNumber= request.POST.get('cardNumber')
        cvv = request.POST.get('cvv')
        pay = Payment(uname=uname,year=year,month=month,cardNumber=cardNumber,cvv=cvv)
        pay.save()
        
        messages.success(request, 'Your message has been sent!')
        return redirect('/order')
        # subject = 'Payment'
        # message = f'Username {uname} Year{year} Month :{month} Cardno: {cardNumber}  CVV {cvv}'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['aryasah30@gmail.com']
        # send_mail(subject, message , email_from ,recipient_list ) 
        # print(message)
        return redirect('/order')
    return render(request, 'accounts/payment.html')
    
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        subject = 'Thank You For Contacting TechArya '
        message = f'Dear {name} : Thank you for contacting with us. We greatly appreciate the time you took to contact us we will soon reach you with reply. You can go to https://aryasahmedicine.herokuapp.com/ '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['aryasah30@gmail.com']
        send_mail(subject, message , email_from ,recipient_list ) 
        messages.success(request, 'Your message has been sent!')
    return redirect('/')
