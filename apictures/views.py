from django.shortcuts import render
from .models import Category, Image, Location
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    return render(request, 'home.html')

def home(request):
    images = Image.objects.all()
    # print(images[0].category)
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'images':images,  "locations": locations,"categories": categories})


def search(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get('image')
        searchname= Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message, "image":searchname})
    else:
        return render(request, 'search.html')


def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
        print(image.category.id)
    except ObjectDoesNotExist:
        
        message = "Image does not exist or may have been deleted!"
        return render(request, 'image.html', {"message":message})
    return render(request, 'image.html', {"image":image})


def category(request, category_id):
    try:
        category = Category.objects.get(id = category_id)
        images = Image.search_image(category)
        message = category.name
        title = category.name
        return render(request, 'search.html',{"title":title, "message":message,"images": images})
    except ObjectDoesNotExist:
        message = "NO ITEMS UNDER CATEGORY " + search.upper()
        categories = Category.objects.all()
        title= "Not Found"
        return render(request, 'search.html',{"title":title,"message":message, "categories": categories})

def location(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
        images = Image.filter_by_location(location)
        message = location.name
        title = location.name
        return render(request, 'search.html',{"title":title, "message":message,"images": images})
    except ObjectDoesNotExist:
        message = "NO ITEMS FOR THAT LOCATION"
        locations = Location.objects.all()
        title= "Not Found"
        return render(request, 'search.html',{"title":title,"message":message, "locations": locations})