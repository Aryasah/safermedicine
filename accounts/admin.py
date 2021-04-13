from django.contrib import admin
from .models import *
from .models import Profile
from .models import Payment
from .models import Contact

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
 list_display = ['id', 'user','is_verified','created_at',]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
 list_display = ['id', 'name','email','phone','desc',]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
 list_display = ['id', 'fname','lname','email','phone','desc','city','medname']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
 list_display = ['id', 'uname','month','year','cardNumber','cvv',]
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
 list_display = ['id', 'picture', 'username', 'profession','comment']
