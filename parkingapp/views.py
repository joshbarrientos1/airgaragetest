
from django.http import HttpResponse
from django.shortcuts import render
from .services import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    location = request.POST.get('location_button')
    businesses = []
    businesses = yelp_call(location=location)
    return render(request, 'parkingapp/index.html', {'results':businesses,})