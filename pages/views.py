from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def projects_view(request):
    return render(request, 'pages/projects_list.html')

def experience(request):
    return render(request, 'content/experience.html')



