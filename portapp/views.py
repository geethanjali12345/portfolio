from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from .models import Contact
from .forms import ContactForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

# class AddProfile(FormView):
# 	model= Contact
# 	# fields='__all__'
# 	form_class=ContactForm
# 	template_name='home.html'
# 	success_url='/'
	# def form_valid(self, form):
	# 	form.send_email()
	# 	return super().form_valid(form)
        # return super().form_valid(form)

def home_view(request): 
    context ={} 
  
    # create object of form 
    form = ContactForm(request.POST or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form']= form 
    return render(request, "home.html", context)