from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})
    # return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
    # return HttpResponse("<h1>Contact Page</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'This is about us',
        'my_number': 123,
        'my_list': [123,12,45,344,789,89, 'abc', 'cde']
    }
    return render(request, 'about.html', my_context)