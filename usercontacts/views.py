from django.shortcuts import render


def add_contact(request):
    return render(request, "index.html")
    
    