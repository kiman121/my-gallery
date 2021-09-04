from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title':'Gallery - home'
    }
    return render(request, 'photos/index.html', context)