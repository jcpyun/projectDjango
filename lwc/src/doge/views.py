from django.conf import settings

from django.contrib import messages    #JUST implemented this myself
from django.core.mail import send_mail

from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = "Early Access:"
	form = SignUpForm(request.POST or None)
	# if request.method=="POST":
	# 	print request.POST
	context = {
		"title": title,
		"form": form,
	}
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)

		full_name= form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name= "Anonymous"
		instance.save()
		#print instance.timestamp
	# if request.user.is_authenticated():
	# 	title= "Hello %s, I've been expecting you" %(request.user)
		context = {
			"title": "Thank You, Your input has been submitted",
		}
	if request.user.is_authenticated() and request.user.is_staff:
		# i = 1
		# for instance in SignUp.objects.all():
		# 	print i, instance
		# 	i +=1
		# print (SignUp.objects.all())
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset":queryset,
		}
	return render(request, "home.html", context) 
	## MAKE SURE TO GO TO URLS.PY AT LWC AND CHANGE TO 
	## DOGE INSTEAD OF LWC.VIEWS.HOME


def contact (request):
	title= 'Contact Us!'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name=form.cleaned_data.get("full_name")

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,"cmujcp@gmail.com"]
		contact_message = "%s: %s via %s"%(
			form_full_name,
			form_message,
			form_email)
		# some_html_message="""
		#<h1>hello</h1>
		#"""
		send_mail(subject,
			contact_message,
			from_email,
			to_email,
			#html_message=some_html_message,
			fail_silently=False)
		# for key ,value in form.cleaned_data.iteritems():
		# 	print key,value
		# email = form.cleaned_data.get("email")
		# message=form.cleaned_data.get("message")
		# full_name=form.cleaned_data.get("full_name")
		# print email,message,full_name
		#send_mail('Subject here', 'Here is the message.', 'from@example.com',
    #['to@example.com'], fail_silently=False)
		

	context = {
		"form" : form,
		"title" : title,

	}
	return render(request, "forms.html", context)



