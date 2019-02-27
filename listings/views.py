from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .choices import state_choices, bedroom_choices, prices_choices


from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing

    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__iconatins = keywords )


    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'prices_choices': prices_choices,
        'listings':queryset_list
    }
    return render(request, 'listings/search.html', context)