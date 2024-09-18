
      
from django.shortcuts import render

from .forms import AdminRegistrationForm,AdminLoginForm
from .models import AdminModel
# Create your views here.
def land(request):
    return render(request,'land.html')

def register(request):
    form = AdminRegistrationForm()
    if request.method=='POST':
        data = AdminRegistrationForm(request.POST)
        if data.is_valid():
            name=data.cleaned_data['admin_name']
            email=data.cleaned_data['admin_email']
            city=data.cleaned_data['admin_city']
            contact=data.cleaned_data['admin_mobile']
            password = data.cleaned_data['admin_password']
            print(name,email,city,contact,password)
            data.save()
            msg="Registration Successfully"
            return render(request,'register.html',{'form':form,'msg':msg})
    else:
        return render(request,'register.html',{'form':form})
    
def login(request):
    form = AdminLoginForm()
    if request.method=="POST":
        data = AdminLoginForm(request.POST)
        if data.is_valid():
            email = data.cleaned_data['admin_email']
            password = data.cleaned_data['admin_password']
            # print(email,password)
            user = AdminModel.objects.filter(admin_email=email)
            
            if user:
                user = AdminModel.objects.get(admin_email=email)
                # print(user.stu_password)
                if user.stu_password==password:
                    name = user.admin_name
                    email = user.admin_email
                    contact = user.admin_mobile
                    city = user.admin_city
                    password = user.admin_password
                    data = {
                        'name':name,
                        'email':email,
                        'contact':contact,
                        'city':city,
                        'password':password
                    }
                  
                    return render(request,'login.html',{'data':data})
                else:
                    msg = "Email & Password not matched"
                    return render(request,'login.html',{'form':form,'msg':msg})
            else:
                msg = "Email not register so please register first"
                return render(request,'login.html',{'form':form,'msg':msg})
    else:
        return render(request,'login.html',{'form':form})
    