from django.shortcuts import render,redirect
from django.views import View
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def homepage(request):
    all_writing = models.Blog.objects.all()
    writing_dict={"writings":all_writing}
    return render(request,'blog_app/home.html',context=writing_dict)

@login_required(login_url="/login")
def addtoblog(request):
    if request.POST:
        message=request.POST["message"]
        models.Blog.objects.create(username=request.user,message=message)
        return redirect(reverse('blog_app:home'))
    else:
        return render(request, 'blog_app/addtoblog.html')



@login_required
def delete(request,id):
    writing=models.Blog.objects.get(pk=id)
    if request.user == writing.username:
        models.Blog.objects.filter(id=id).delete()
        return redirect('blog_app:home')


class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"
