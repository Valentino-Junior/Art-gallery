from django.shortcuts import render
from .models import Image, Location

def welcome(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render (request,'home.html' , {'images': images[::-1], 'locations': locations} )

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't browsed at any of the image categories yet."
        return render(request, 'search.html', {"message": message})


# Create your views here.
def nav(request):
    return render (request,'navbar.html' )

def base(request):
    return render (request,'base.html' )