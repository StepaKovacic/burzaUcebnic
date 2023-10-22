from django.shortcuts import render
from .models import Offer
# Create your views here.
def home(request):
	offers = Offer.objects.all()


	return render(request, "home.html", {'offers':offers})


def create(request):
	if request.method == "POST":
		pass

