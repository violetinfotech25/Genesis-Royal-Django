from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def doctorpage (request):
    return render (request, 'main/Doctorpage.html')

def drgobinathan(request):
    return render(request, 'main/dr.gobinathan.html')

def drchadrakala(request):
    return render(request, 'main/dr.chandrakala.html')