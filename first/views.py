from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm,SignUpForm
# Create your views here.
def indexs(request):
	title='Welcome New User'
	form=SignUpForm(request.POST or None)
	cont={
		'title':title,
		"form":form,}
	if form.is_valid():
		instance=form.save()
		cont={'title':'Thank You',}

	if request.user.is_authenticated():
		title="Welcome Mr. %s" %(request.user)
	
	
	return render(request,'forms.html',cont)

def contact(request):
	form=ContactForm(request.POST or None)



	if form.is_valid():
		#print form.cleaned_data
		f_email=form.cleaned_data.get('email')
		f_mesg=form.cleaned_data.get('message')
		f_full_name=form.cleaned_data.get('full_name')
		subject='Site form data'
		from_email=settings.EMAIL_HOST_USER
		to_email=[from_email]
		contact_message="%s %s via %s"%(f_full_name,f_mesg,f_email)
		send_mail(subject,contact_message,from_email,to_email,fail_silently=False)
	context={'form':form}

	return render(request,'forms.html',context)