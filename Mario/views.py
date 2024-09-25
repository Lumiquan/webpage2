from django.shortcuts import render
from .models import NewProfile


def squad(request):  
        
    if request.method == 'POST':
        username = request.POST.get('username')
        about = request.POST.get('about')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        street_address = request.POST.get('street-address')
        city = request.POST.get('city')
        region = request.POST.get('region')
        postal_code = request.POST.get('postal-code')
        Profileinfo = NewProfile(username =username, about =about, first_name= first_name, last_name= last_name, email= email, country= country, street_address= street_address, city= city, state_province= region, zipcode= postal_code)
        Profileinfo.save()


    return render(request, 'Mario/Ayo.html')

def Mariolist(request):
  
    Mariodata = NewProfile.objects.all()
    context= {'Mariodata':Mariodata}

    return render(request, 'Mario/Mariolist.html', context)