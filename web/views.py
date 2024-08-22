from django.shortcuts import render, redirect
from web.models import Flan, Contact 
from web.forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    """ flanes=Flan.objects.all()
    flanes_privados=Flan.objects.filter(is_private=True) """
    flanes_publicos=Flan.objects.filter(is_private=False)
    context={
        'flanes_pub':flanes_publicos
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    """ flanes=Flan.objects.all()     
    flanes_publicos=Flan.objects.filter(is_private=False)"""
    flanes_privados=Flan.objects.filter(is_private=True)
    context={
        'flanes_pri':flanes_privados
    }
    return render(request, 'welcome.html', context)

def contact(request):
    if request.method=="GET":
        form=ContactFormModelForm()
        context={'form':form}
        return render(request, 'contact.html', context)
    else:
        form=ContactFormModelForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                **form.cleaned_data
            )
            return redirect('exito')
        context={'form':form}
        return render(request, 'contact.html', context)
    
def success(request):
    return render(request, 'exito.html')
        




