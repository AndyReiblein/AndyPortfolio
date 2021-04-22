from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import pdb
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')


def contact(request):
	if request.method == 'POST':
		# pdb.set_trace()

		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'andrewmreiblein013@gmail.com', ['andrewmreiblein013@gmail.com'], fail_silently=False) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
            messages.success(request, f'Account created for {username}!')
			return redirect("/")
			

			
			
            
           
	form = ContactForm()
	return render(request, "contact.html", {'form':form})

def about(request):
    return render(request, 'about.html')

def messages(request):
	return render(request, 'messages.html')