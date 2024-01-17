from django.shortcuts import redirect,render
from django.http import JsonResponse 
from calend.models import Reserve
from .forms import ReservationForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
 
 
@login_required(login_url='login')
def index(request):  
    all_events = Reserve.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'index.html',context)
 
def all_events(request):                                                                                                 
    all_events = Reserve.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Reserve(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Reserve.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Reserve.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


def Home(request):
    return render(request,'Home.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def Logout(request):
    logout(request)
    return redirect('login')

def Login(request):
    if request.method =="POST":
       username = request.POST["username"]
       password = request.POST["password"]
       user = authenticate(request, username=username, password=password)
       if user is not None:
         login(request, user)
         return redirect('index')   
       else:
         messages.success(request,("There was an error loggin In ,try again "))
         return redirect('login')
    else:
        return render(request,'Login.html')
    
def Register(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
         form.save()
         username = form.cleaned_data['username']
         password = form.cleaned_data['password1']
         user = authenticate(username=username,password=password)
         login(request,user)
         messages.success(request,"registration is successful")
         return redirect('home')
    else:
        form= UserCreationForm()
    return render(request,"Register.html",{'form':form})


@login_required(login_url='login')
def ReservationCreate(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            salle=form.cleaned_data.get('salle')
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'Reserver.html', {'form': form})
