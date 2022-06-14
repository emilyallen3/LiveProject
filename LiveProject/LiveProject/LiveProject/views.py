from django.shortcuts import render

def magic_home(request):
    return render(request, 'magic_home.html')

