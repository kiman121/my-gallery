from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from .models import Image, Category, Location

# Create your views here.
def home(request):
    context = {
        'title': 'Gallery - home',
        'gallery': Image.get_gallery()
    }
    return render(request, 'photos/index.html', context)

def all_categories_gallery(request):
    '''
    View function that renders gallery by categories
    '''
    num_records_by_category = Category.objects.annotate(records=Count('image'))
    context = {
        'title': 'Gallery - by category',
        'gallery': Image.get_gallery(),
        'categories': num_records_by_category
    }

    return render(request, 'photos/all-categories-gallery.html', context)

def gallery_by_category(request, category_id):
    '''
    View function that renders gallery by category id
    '''
    category = Category.get_category_by_id(category_id)
    gallery = Image.get_category_gallery(category)

    context = {
        'title':'Gallery - '+ category.name,
        'gallery': gallery,
        'category': category.name
    }

    return render(request, 'photos/by-category-gallery.html', context)

def all_locations_gallery(request):
    '''
    View function that renders gallery by locations
    '''
    num_records_by_location = Location.objects.annotate(records=Count('image'))
    context = {
        'title': 'Gallery - by location',
        'gallery': Image.get_gallery(),
        'locations': num_records_by_location
    }

    return render(request, 'photos/all-locations-gallery.html', context)

def gallery_by_location(request, location_id):
    '''
    View function that renders gallery by location id
    '''
    location = Location.get_location_by_id(location_id)
    gallery = Image.get_location_gallery(location)

    context = {
        'title':'Gallery - '+ location.name,
        'gallery': gallery,
        'location': location.name
    }

    return render(request, 'photos/by-location-gallery.html', context)


def search_category(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        try:
            match_category = Category.search_category(search_term)
            gallery = Image.search_gallery(match_category)
            message = f'{search_term}'

            context = {
                'title':'Gallery - search',
                'gallery': gallery,
                'message': message,
            }
        except:
            message = f'Your search - {search_term} - did not match any category'
            context = {
                'title':'Gallery - search',
                'message': message,
            }
        return render(request, 'photos/search.html', context)
    else:
        message = "Your search request does not have any category!"
        context = {
            'title':'Gallery - search',
            'message': message,
        }
        return render(request, 'photos/search.html', context)

def photo_detail(request, photo_id):
    # photo_id = request.GET.get('id')
    photo = Image.get_gallery_item(photo_id)
    data = {
        'id': photo.id,
        'name': photo.name,
        'location': photo.location.name,
        'description': photo.description,
        'image_url': photo.image.url,
        'category': photo.category.name
    }
    return JsonResponse(data)