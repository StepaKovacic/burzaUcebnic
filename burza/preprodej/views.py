from django.shortcuts import render
from .models import Offer, Book
from .forms import SearchForm
from json import dumps

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

	books = list(Book.objects.values())
	return render(request, "home.html", {'offers':offers,'form':emptyForm, 'books':dumps(books)})


def create(request):
	if request.method == "POST":
		pass
