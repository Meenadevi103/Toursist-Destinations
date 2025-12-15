from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Destination
from django.http import HttpResponseForbidden

# Create your views here.
from django.contrib.auth.hashers import make_password
# @login_required
# def home(request):
#     return render(request,'accounts/home.html')
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('destination_list')  # THIS IS CORRECT!
        else:
            return render(request, 'accounts/login.html', {
                'error': 'invalid username or password'
            })

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# @login_required
# def home(request):
#     return render(request,'accounts/home.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get("email")
        password = request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password!=confirm_password:
            return render(request,'accounts/register.html',{
                'error':'passwords do not match'
            })
        if User.objects.filter(username=username).exists():
            return render(request,'accounts/register.html',{
                'error':'username already exists'
            })
        user=User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        return redirect('login')
    return render(request, 'accounts/register.html')


@login_required
def destination_list(request):
    destinations = Destination.objects.all().order_by('-created_at')
    return render(request, 'accounts/list.html', {'destinations': destinations})

# @login_required
# def destination_detail(request,pk):
#     destination=get_object_or_404(Destination,pk=pk)
#     return render(request,'destination/detail.html',{'destination':destination})

@login_required
def destination_create(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only tourism officers can add destinations")
    if request.method=='POST':
        place_name=request.POST.get('place_name')
        weather = request.POST.get('weather')
        state = request.POST.get('state')
        district = request.POST.get('district')
        google_map_link = request.POST.get('map')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Destination.objects.create(
            place_name=place_name,
            weather=weather,
            state=state,
            district=district,
            google_map_link=google_map_link,
            description=description,
            image=image
        )
        return redirect('destination_list')
    return render(request,'accounts/create.html')


@login_required
def destinaton_update(request,pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only tourism officers can update destinations")
    destination=get_object_or_404(Destination,pk=pk)
    if request.method=='POST':
        destination.place_name=request.POST.get('place_name')
        destination.weather = request.POST.get('weather')
        destination.state = request.POST.get('state')
        destination.district = request.POST.get('district')
        destination.google_map_link = request.POST.get('google_map_link')
        destination.description = request.POST.get('description')

        if request.FILES.get('image'):
            destination.image = request.FILES.get('image')
        destination.save()
        return redirect('destination_list')
    return render(request,'accounts/update.html',{'destination':destination})


# DELETE VIEW
@login_required
def destination_delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only tourism officers can delete destinations")

    destination = get_object_or_404(Destination, pk=pk)

    if request.method == "POST":
        destination.delete()
        return redirect('destination_list')

    return render(request, 'accounts/delete.html', {'destination': destination})
