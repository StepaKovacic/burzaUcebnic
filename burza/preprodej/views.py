from django.shortcuts import render
from .models import Offer, Book
from .forms import SearchForm

# Create your views here.
def home(request):
	emptyForm = SearchForm()
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			books = Book.objects.filter(name__startswith = form.cleaned_data['search'])
			offers = []
			for book in books:
				offers += Offer.objects.filter(book = book)

		return render(request,'home.html',context={'offers':offers,'form':emptyForm})
	offers = Offer.objects.all()

	
	return render(request, "home.html", {'offers':offers,'form':emptyForm})


def create(request):
	if request.method == "POST":
		pass

