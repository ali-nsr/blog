from django.shortcuts import render
from .models import ContactUs
from site_settings.models import SiteSettings, AboutUs
from .forms import CreateContactForm


def contact_us(request):
    contact_form = CreateContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')

        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        contact_form = CreateContactForm()

    context = {
        'contact_form': contact_form,
        'site_settings': SiteSettings.objects.first(),
    }

    return render(request, 'contact_us/contact_us.html', context)


def about_us(request):
    context = {
        'about': AboutUs.objects.first(),
    }
    return render(request, 'contact_us/about_us.html', context)
