from django.shortcuts import render, redirect
from .models import Home, About, Profile, Category, Skills, Portfolio
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolios
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['mg.sharp@mail.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients, fail_silently=False,
                      auth_user=None, auth_password=None, connection=None, html_message=None)
            messages.add_message(request, messages.INFO,
                                 'Thank You! Your message was successfully sent!')
            return redirect('/#contact')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'index.html', context)
