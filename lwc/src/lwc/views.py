
from django.shortcuts import render

# Create your views here.
def about(request):
	
	return render(request, "about.html", {}) 


# from django.shortcuts import render

# def home(request):
# 	context = {}
# 	template = "home.html"
# 	return render(request, template, context)

# # def home2(request):
# # 	context = {}
# # 	template = "home2.html"
# # 	return render(request, template, context)