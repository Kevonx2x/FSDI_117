from django.shortcuts import render

# Create your views here.
def projects_list(request):
    return render(request, 'content/projects_list.html')

def experience_list(request):
    return render(request, "content/experience_list.html")