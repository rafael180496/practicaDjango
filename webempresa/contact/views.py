from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from  django.urls import reverse
from .forms import ContactForm
# Create your views here.


def contact(request):
    contacto_form = ContactForm()

    if request.method =='POST':
        contacto_form = ContactForm(data=request.POST)
        if contacto_form.is_valid():
            name=request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviar el correo
            try:
                emailSend(name,content,email).send()
                #toodo bien se redireccionea    
                return redirect(reverse('contact')+'?ok')
            except Exception:
                return redirect(reverse('contact')+'?fail')
    return render(request, "contact/contact.html", {'form': contacto_form})

def emailSend(name,content,email):
    email=EmailMessage(
        "La Caffettiera: Nueva mensaje  de contacto",
        "De {} <{}> \n\n Escribio:\n\n{}".format(name,email,content),
        "no-contestar@inbox.mailtrap.io",
        ["rafael180496@gmail.com"],
        reply_to=[email]
    )
    return email
