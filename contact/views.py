from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from contact.forms import forms 


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST or None) # A form bound to the POST data
        if form.is_valid():
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    recipients = settings.RECIPIENTS
	    if cc_myself:
	        recipients.append(sender)

	    send_mail(subject, message, sender, recipients)
	    return HttpResponseRedirect('/thankyou/') # Redirect after POST # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thankyou/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, '/contact/', {'form': form})
