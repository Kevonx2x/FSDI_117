from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def projects_view(request):
    return render(request, 'pages/projects_list.html')

def experience(request):
    return render(request, 'content/experience.html')

def contact_view(request):
    if request.method == "POST":
        #send message
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                "Email from " + name,
                message, 
                email,
                ['turonboyd16@gmail.com']
            )



        else:
            print("Invalid Form")
    else:
        # display page
        form = ContactForm()
        

    return render(request, "pages/contact.html", {'form': form})



